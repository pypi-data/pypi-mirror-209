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

import copy
from pathlib  import Path
from argparse import Namespace
from typing import Dict, Any, Tuple, Optional
from dataclasses import asdict

import json

from .base import QnAPreprocessArgs, QnADataset
from ....nlp_auto.config import AzuremlAutoConfig
from ....nlp_auto.tokenizer import AzuremlAutoTokenizer
from ....constants.constants import Tasks, DatasetSplit, SaveFileConstants, MLFlowHFFlavourConstants

from azureml.acft.accelerator.utils.logging_utils import get_logger_app
from azureml.acft.accelerator.utils.error_handling.exceptions import ValidationException
from azureml.acft.accelerator.utils.error_handling.error_definitions import InvalidDataset, InvalidLabel, TokenizerNotSupported
from azureml._common._error_definition.azureml_error import AzureMLError  # type: ignore

from transformers.tokenization_utils_base import PreTrainedTokenizerBase
from transformers.tokenization_utils_fast import PreTrainedTokenizerFast


logger = get_logger_app()


class QnAPreprocessForFinetune:

    def __init__(self, component_args: Namespace, preprocess_args: QnAPreprocessArgs) -> None:
        # component args is combined args of
        #  - preprocess component args
        #  - model_name arg from model selector
        #  - newly constructed model_name_or_path
        self.component_args = component_args
        self.preprocess_args = preprocess_args

        logger.info(f"Task name: {Tasks.QUESTION_ANSWERING}")

        self.model_type = AzuremlAutoConfig.get_model_type(hf_model_name_or_path=component_args.model_name_or_path)
        logger.info(self.preprocess_args)

        self.tokenizer = self._init_tokenizer()

    def _init_tokenizer(self) -> PreTrainedTokenizerBase:
        """Initialize the tokenizer and set the model max length for the tokenizer if not already set"""

        tokenizer_params = {
            "task_name": Tasks.QUESTION_ANSWERING,
            "apply_adjust": True,
            "max_sequence_length": self.preprocess_args.max_seq_length
        }

        tokenizer = AzuremlAutoTokenizer.from_pretrained(self.component_args.model_name_or_path, **tokenizer_params)

        # Only FastTokenizer is supported for QA
        # The python based tokenizer doesn't support `return_offsets_mapping=True`
        if not isinstance(tokenizer, PreTrainedTokenizerFast):
            raise ValidationException._with_error(
                AzureMLError.create(
                    TokenizerNotSupported, Tokenizer=tokenizer, TaskName=Tasks.QUESTION_ANSWERING
                )
            )
        return tokenizer

    def _get_encode_dataset_params(self) -> Dict[str, Any]:

        encode_params = {}
        pad_on_right = self.tokenizer.padding_side == "right"
        # padding and truncation
        encode_params["padding"] = "max_length"
        if pad_on_right:
            encode_params["truncation"] = "only_second"
        else:
            encode_params["truncation"] = "only_first"

        # max sequence length
        # Refer to the link for understanding how max_length is chosen
        # https://github.com/huggingface/transformers/blob/5764efe544de909e93bfde16489b5a0975fce1c2/src/transformers/pipelines/question_answering.py#L403
        encode_params["max_length"] = min(384, self.tokenizer.model_max_length)

        return encode_params

    def _load_data_splits(self, save_raw_data: bool = False) -> Optional[Tuple[str, str, str]]:
        """
        1. Load train, validation and test data splits
        2. Add column prefix for the data
        """
        # encode params used for encoding dataset
        self.encode_params = self._get_encode_dataset_params()

        # initialize dataset
        dataset_args = asdict(self.preprocess_args)
        dataset_args.update(self.encode_params)
        kwargs = dict(
            dataset_args=dataset_args,
            required_columns=self.preprocess_args.required_columns,
            nested_columns=self.preprocess_args.nested_columns,
            required_column_dtypes=self.preprocess_args.required_column_dtypes,
            label_column=self.preprocess_args.label_column,
            tokenizer=self.tokenizer,
        )
        logger.info("Loading train dataset")
        self.train_ds = QnADataset(
            self.component_args.train_data_path,
            **copy.deepcopy(kwargs),
            slice=self.component_args.train_slice,
        )
        logger.info("Loading validation dataset")
        self.valid_ds = QnADataset(
            self.component_args.validation_data_path,
            **copy.deepcopy(kwargs),
            slice=self.component_args.validation_slice,
        )
        if self.component_args.test_data_path is not None:
            logger.info("Loading test dataset")
            self.test_ds = QnADataset(
                self.component_args.test_data_path,
                **copy.deepcopy(kwargs),
                label_column_optional=False,
                slice=self.component_args.test_slice,
            )
        else:
            self.test_ds = None

        # save raw data
        if save_raw_data:
            (
                raw_train_data_fname,
                raw_validation_data_fname,
                raw_test_data_fname
            ) = self._save_raw_data()

        # add dataset prefix
        self.train_ds.update_dataset_columns_with_prefix()
        self.train_ds.update_required_columns_with_prefix()
        self.valid_ds.update_dataset_columns_with_prefix()
        self.valid_ds.update_required_columns_with_prefix()
        if not self.component_args.skip_test_data_processing and self.test_ds is not None:
            self.test_ds.update_dataset_columns_with_prefix()
            self.test_ds.update_required_columns_with_prefix()

        if save_raw_data:
            return (raw_train_data_fname, raw_validation_data_fname, raw_test_data_fname)

    def _save_raw_data(self) -> Tuple[str, str, Optional[str]]:
        # save the raw train and valid dataset
        # NOTE call this function before encoding the dataset else this will save encoded datasaet
        logger.info("Saving the raw datasets")
        raw_folder_name = "raw_data"
        raw_data_save_folder = str(Path(self.component_args.output_dir, raw_folder_name))
        raw_train_data_fname = str(
            Path(
                raw_folder_name,
                self.train_ds.save(
                    save_folder=raw_data_save_folder,
                    save_name=DatasetSplit.TRAIN,
                    batch_size=self.preprocess_args.batch_size
                )
            )
        )
        raw_validation_data_fname = str(
            Path(
                raw_folder_name,
                self.valid_ds.save(
                    save_folder=raw_data_save_folder,
                    save_name=DatasetSplit.VALIDATION,
                    batch_size=self.preprocess_args.batch_size
                )
            )
        )
        raw_test_data_fname = None
        if self.test_ds is not None:
            raw_test_data_fname = str(
                Path(
                    raw_folder_name,
                    self.test_ds.save(
                        save_folder=raw_data_save_folder,
                        save_name=DatasetSplit.TEST,
                        batch_size=self.preprocess_args.batch_size
                    )
                )
            )

        return (raw_train_data_fname, raw_validation_data_fname, raw_test_data_fname)

    def _validate_data_splits(self):
        """validate the datasets"""
        # validate the datasets
        logger.info("Validating the train dataset")
        self.train_ds.validate()
        logger.info("Validating the validation dataset")
        self.valid_ds.validate()
        if not self.component_args.skip_test_data_processing and self.test_ds is not None:
            logger.info("Validating the test dataset")
            self.test_ds.validate()

    def _encode_data_splits(self):
        """
        Encode the dataset
        """
        logger.info("Encoding the train dataset")
        self.train_ds.encode_dataset()
        logger.info("Encoding the validation dataset")
        self.valid_ds.encode_dataset()
        if not self.component_args.skip_test_data_processing and self.test_ds is not None:
            logger.info("Encoding the test dataset")
            self.test_ds.encode_dataset()

    def preprocess(self) -> None:
        """
        Preprocess the raw dataset
        """

        # load, validate the datasets
        (
            raw_train_data_fname,
            raw_validation_data_fname,
            raw_test_data_fname
        ) = self._load_data_splits(save_raw_data=True)
        self._validate_data_splits()

        # encode the dataset
        self._encode_data_splits()

        # Save
        # 1. encoded datasets
        # 2. Arguments
        # 3. tokenizer
        # 4. mlflow inference data

        # 1. Encoded datasets
        logger.info("Saving the encoded datasets")
        encoded_train_data_fname = self.train_ds.save(
            save_folder=self.component_args.output_dir,
            save_name=DatasetSplit.TRAIN,
            batch_size=self.preprocess_args.batch_size
        )
        encoded_validation_data_fname = self.valid_ds.save(
            save_folder=self.component_args.output_dir,
            save_name=DatasetSplit.VALIDATION,
            batch_size=self.preprocess_args.batch_size
        )
        if not self.component_args.skip_test_data_processing and self.test_ds is not None:
            encoded_test_data_fname = self.test_ds.save(
                save_folder=self.component_args.output_dir,
                save_name=DatasetSplit.TEST,
                batch_size=self.preprocess_args.batch_size
            )

        # 2. Arguments: save the preprocess args, model_type, encoded datasets
        preprocess_args = vars(self.component_args)
        preprocess_args.update(vars(self.preprocess_args))
        # add the model path
        preprocess_args["model_type"] = self.model_type
        # add the paths for raw train, validation and test paths
        preprocess_args["raw_train_data_fname"] = raw_train_data_fname
        preprocess_args["raw_validation_data_fname"] = raw_validation_data_fname
        # Only processing the test data is controlled using the flag; we will still save the raw dataset for test
        if self.test_ds is not None:
            preprocess_args["raw_test_data_fname"] = raw_test_data_fname
        # add the paths for encoded train, validation and test paths
        preprocess_args["encoded_train_data_fname"] = encoded_train_data_fname
        preprocess_args["encoded_validation_data_fname"] = encoded_validation_data_fname
        if not self.component_args.skip_test_data_processing and self.test_ds is not None:
            preprocess_args["encoded_test_data_fname"] = encoded_test_data_fname
        preprocess_args_save_path = Path(self.component_args.output_dir, SaveFileConstants.PREPROCESS_ARGS_SAVE_PATH)
        logger.info(f"Saving the preprocess args to {preprocess_args_save_path}")
        preprocess_args["model_name_or_path"] = str(preprocess_args["model_name_or_path"])
        with open(preprocess_args_save_path, 'w') as fp:
            json.dump(preprocess_args, fp, indent=2)

        # 3. tokenizer
        self.tokenizer.save_pretrained(self.component_args.output_dir)

        # 4. save the mlflow inference params
        save_key = MLFlowHFFlavourConstants.INFERENCE_PARAMS_SAVE_KEY
        save_data = {
            save_key: self.encode_params
        }
        mlflow_inference_params_save_path = Path(
            self.component_args.output_dir, MLFlowHFFlavourConstants.INFERENCE_PARAMS_SAVE_NAME_WITH_EXT)
        logger.info(f"Saving the mlflow inference params at {mlflow_inference_params_save_path}")
        with open(mlflow_inference_params_save_path, 'w') as wptr:
            json.dump(save_data, wptr)
