# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
# Copyright 2020 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ---------------------------------------------------------

import json
import numpy as np
from pathlib import Path
from functools import partial

from typing import Any, Dict, List, Tuple, Optional

from ..preprocess.base import SummarizationDataset
from ....constants.constants import SaveFileConstants, MLFlowHFFlavourConstants, TaskConstants, Tasks
from ....nlp_auto.model import AzuremlAutoModelForSummarization
from ....nlp_auto.tokenizer import AzuremlAutoTokenizer
from ....utils.mlflow_utils import SaveMLflowModelCallback, replace_deepspeed_zero3_mlflow_pytorch_weights

import torch.nn as nn
import nltk

from azureml.acft.accelerator.utils.logging_utils import get_logger_app

from azureml.acft.accelerator.finetune import AzuremlFinetuneArgs, AzuremlDatasetArgs
from azureml.acft.accelerator.finetune import AzuremlTrainer
from azureml.acft.accelerator.constants import HfTrainerType

from datasets.load import load_metric

from transformers.tokenization_utils_base import PreTrainedTokenizerBase
from transformers.trainer_utils import EvalPrediction
from transformers.models.mbart.tokenization_mbart import MBartTokenizer
from transformers.models.mbart.tokenization_mbart_fast import MBartTokenizerFast
from transformers.models.mbart50.tokenization_mbart50 import MBart50Tokenizer
from transformers.models.mbart50.tokenization_mbart50_fast import MBart50TokenizerFast
from transformers.deepspeed import is_deepspeed_zero3_enabled

MULTILINGUAL_TOKENIZERS = [MBartTokenizer, MBartTokenizerFast, MBart50Tokenizer, MBart50TokenizerFast]


logger = get_logger_app()


class SummarizationFinetune:

    def __init__(self, finetune_params: Dict[str, Any]) -> None:
        # finetune params is finetune component args + args saved as part of preprocess
        self.finetune_params = finetune_params

        logger.info(f"Task name: {Tasks.SUMMARIZATION}")

        # set predict_with_generate=True for Summarization
        self.finetune_params["predict_with_generate"] = True

        # set log_metrics_at_root=False to not to log to parent
        self.finetune_params["log_metrics_at_root"] = False

    def _get_finetune_args(self, model_type: str) -> AzuremlFinetuneArgs:

        self.finetune_params["model_type"] = model_type
        azml_trainer_finetune_args = AzuremlFinetuneArgs(
            self.finetune_params,
            trainer_type=HfTrainerType.SEQ2SEQ
        )

        return azml_trainer_finetune_args

    def _get_dataset_args(self, tokenizer: Optional[PreTrainedTokenizerBase] = None) -> AzuremlDatasetArgs:

        encoded_train_ds = SummarizationDataset(
            str(Path(self.finetune_params["preprocess_output"], self.finetune_params["encoded_train_data_fname"])),
            tokenizer=tokenizer
        )
        encoded_validation_ds = SummarizationDataset(
            str(Path(self.finetune_params["preprocess_output"], self.finetune_params["encoded_validation_data_fname"])),
        )
        azml_trainer_dataset_args = AzuremlDatasetArgs(
            train_dataset=encoded_train_ds.dataset,
            validation_dataset=encoded_validation_ds.dataset,
            data_collator=encoded_train_ds.get_collation_function()
        )

        return azml_trainer_dataset_args

    def _load_model(self, tokenizer: PreTrainedTokenizerBase) -> Tuple[nn.Module, str, List[str]]:

        model_params = {
            "tok_prefix": self.finetune_params["tok_prefix"],
            "ignore_mismatched_sizes": self.finetune_params["ignore_mismatched_sizes"],
            "resume_from_checkpoint": self.finetune_params["resume_from_checkpoint"],
        }

        # load the model
        model, model_type, new_initalized_layers = AzuremlAutoModelForSummarization.from_pretrained(
            self.finetune_params["model_name_or_path"], **model_params)

        if isinstance(tokenizer, tuple(MULTILINGUAL_TOKENIZERS)):
            model.config.forced_bos_token_id = tokenizer.lang_code_to_id[tokenizer.tgt_lang]
            logger.info(f"`config.forced_bos_token_id` is set to {model.config.forced_bos_token_id}")

        return model, model_type, new_initalized_layers

    def _get_tokenizer(self) -> PreTrainedTokenizerBase:
        """This method loads the tokenizer as is w/o any modifications to it"""

        tokenizer_params = {
            "apply_adjust": False,
            "task_name": self.finetune_params["task_name"],
        }

        return AzuremlAutoTokenizer.from_pretrained(self.finetune_params["preprocess_output"], **tokenizer_params)

    def finetune(self) -> None:

        # configure MLflow save callback
        mlflow_infer_params_file_path = Path(
            self.finetune_params["preprocess_output"], MLFlowHFFlavourConstants.INFERENCE_PARAMS_SAVE_NAME_WITH_EXT
        )
        save_mlflow_callback = SaveMLflowModelCallback(
            mlflow_infer_params_file_path=mlflow_infer_params_file_path,
            mlflow_model_save_path=self.finetune_params["mlflow_model_folder"],
            mlflow_task_type=self.finetune_params["mlflow_task_type"],
            model_name=self.finetune_params["model_name"],
            model_name_or_path=self.finetune_params["model_name_or_path"],
        )

        # load the tokenizer
        tokenizer = self._get_tokenizer()
        # load the model
        model, model_type, new_initialized_params = self._load_model(tokenizer)

        trainer = AzuremlTrainer(
            finetune_args=self._get_finetune_args(model_type),
            dataset_args=self._get_dataset_args(tokenizer),
            model=model,
            tokenizer=tokenizer,
            metric_func=partial(
                summarization_metrics_func,
                tokenizer=tokenizer
            ),
            new_initalized_layers=new_initialized_params,
            custom_trainer_callbacks=[save_mlflow_callback],
        )

        # Torch barrier is used to complete the training on a distributed setup
        # Use callbacks for adding steps to be done at the end of training
        # NOTE Avoid adding any logic after trainer.train()
        # Test the distributed scenario in case you add any logic beyond trainer.train()
        trainer.train()

        # replace pytorch weights for lora / deep speed zero3 optimization
        if trainer.should_save and (self.finetune_params["apply_lora"] or is_deepspeed_zero3_enabled()):
            logger.info("Replacing dummy MLflow weights ")
            replace_deepspeed_zero3_mlflow_pytorch_weights(
                self.finetune_params["pytorch_model_folder"],
                self.finetune_params["mlflow_model_folder"]
            )

        # save files only once by Rank-0 process
        if trainer.should_save:
            # save finetune args
            Path(self.finetune_params["pytorch_model_folder"]).mkdir(exist_ok=True, parents=True)
            finetune_args_path = Path(
                self.finetune_params["pytorch_model_folder"], SaveFileConstants.FINETUNE_ARGS_SAVE_PATH)
            self.finetune_params["model_name_or_path"] = str(self.finetune_params["model_name_or_path"])
            with open(finetune_args_path, 'w') as rptr:
                json.dump(self.finetune_params, rptr, indent=2)


def summarization_metrics_func(eval_pred: EvalPrediction, tokenizer: PreTrainedTokenizerBase):
    """
    compute and return metrics for summarization
    """

    metric = load_metric("rouge")
    predictions, labels = eval_pred
    decoded_preds = tokenizer.batch_decode(predictions, skip_special_tokens=True)
    # Replace -100 in the labels as we can't decode them.
    labels = np.where(labels != TaskConstants.SUMMARIZATION_IGNORE_INDEX, labels, tokenizer.pad_token_id)
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)

    # Rouge expects a newline after each sentence
    decoded_preds = ["\n".join(nltk.sent_tokenize(pred.strip())) for pred in decoded_preds]
    decoded_labels = ["\n".join(nltk.sent_tokenize(label.strip())) for label in decoded_labels]

    logger.info(f"Predictions count: {len(decoded_preds)} | References count: {len(decoded_labels)}")
    result = metric.compute(predictions=decoded_preds, references=decoded_labels, use_stemmer=True)
    # Extract a few results
    result = {key: value.mid.fmeasure * 100 for key, value in result.items()}

    # Add mean generated length
    prediction_lens = [np.count_nonzero(pred != tokenizer.pad_token_id) for pred in predictions]
    result["gen_len"] = np.mean(prediction_lens)

    return {k: round(v, 4) for k, v in result.items()}
