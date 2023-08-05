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
"""
preprocess utils
"""

import os
import json
import numpy as np

from azureml.acft.accelerator.utils.logging_utils import get_logger_app
from ..constants.constants import AutomlConstants, DataConstants

logger = get_logger_app()


# AutoML NLP tasks

def get_new_file_name(path, old_format, new_format):
    prefix = os.path.splitext(path)[0]
    old_name = prefix.split('/')[-1]
    return f'./{old_format}_{old_name}.{new_format}'


def txt_to_jsonl(txt_file, name):
    with open(txt_file, encoding=DataConstants.ENCODING, errors=DataConstants.ERRORS) as f:
        data = f.read()

    with open(name, 'w') as output_file:
        data = data.replace("-DOCSTART- O\n\n", "")
        # separate each sentence
        data = data.split("\n\n")

        for idx in range(len(data)):
            # separate each sentence's tokens
            tokens = data[idx].split('\n')
            new_list = [item.split(" ") for item in tokens if item not in AutomlConstants.NER_IGNORE_TOKENS]

            jsonl_line = {'id': idx, AutomlConstants.TEXT_NER_TOKEN_KEY: [], AutomlConstants.TEXT_NER_TAG_KEY: []}
            for token, tag in new_list:
                jsonl_line[AutomlConstants.TEXT_NER_TOKEN_KEY].append(token)
                jsonl_line[AutomlConstants.TEXT_NER_TAG_KEY].append(tag)
            json.dump(jsonl_line, output_file)
            output_file.write('\n')


def concat_text_columns(example, label_columns, pass_through_columns=None, ignore_columns=None, dataset_columns=None):
    """
    Concatenate all text columns present in a single training example.
    """
    if pass_through_columns:
        pass_through_columns = set(pass_through_columns + label_columns)
    else:
        pass_through_columns = set(label_columns)

    if ignore_columns:
        ignore_columns = set(ignore_columns)
    else:
        ignore_columns = set()
    example_columns = set([col for col in example])
    if dataset_columns:
        dataset_columns = set(dataset_columns).intersection(example_columns)
    else:
        dataset_columns = example_columns
    dataset_columns = dataset_columns.difference(ignore_columns)

    text_columns = dataset_columns.difference(pass_through_columns)
    input_col_entries = [str(example[col]) for col in text_columns]
    
    new_input = ". ".join(input_col_entries)
    new_example = {AutomlConstants.TEXT_CLASSIFICATION_COLUMN_NAME: new_input}
    for label_col in pass_through_columns.intersection(dataset_columns):
        new_example[label_col] = example[label_col]
    return new_example


def get_max_seq_length(train_data,
                       tokenizer,
                       enable_long_range_text) -> int:
    """
    Default value for max_seq_length is 128.

    If the user opts in for long range text, we use this heuristic to determine optimal max_seq_length value.

    If the fraction of training examples with length of the text document exceeding 128 tokens/words
    is greater than an empirically determined threshold, then use a higher value for max_seq_length.
    Currently it gets set to 256 rather than 128 if the aforementioned condition is satisfied.
    """
    max_seq_length = AutomlConstants.DEFAULT_SEQ_LEN
    if enable_long_range_text:
        text_len = []
        for row in train_data:
            concatenated_text = row[AutomlConstants.TEXT_CLASSIFICATION_COLUMN_NAME]
            tokenized = tokenizer.tokenize(concatenated_text)
            text_len.append(len(tokenized))

        default_range_frac = sum(i > AutomlConstants.DEFAULT_SEQ_LEN for i in text_len) / len(text_len)
        long_range_frac = sum(i > AutomlConstants.LONG_RANGE_MAX for i in text_len) / len(text_len)
        logger.info(
            f"Dataset Stats: Mean length of text={np.mean(text_len)}\n"
            f"Max length of text={np.max(text_len)}\n"
            f"Median length of text={np.median(text_len)}\n"
            f"Fraction of number of rows with len of text longer than "
            f"{max_seq_length} tokens={default_range_frac}\n"
            f"Fraction of number of rows with len of text longer than "
            f"{AutomlConstants.LONG_RANGE_MAX} tokens={long_range_frac}"
        )

        if default_range_frac >= AutomlConstants.MIN_PROPORTION_LONG_RANGE:
            max_seq_length = AutomlConstants.LONG_RANGE_MAX
    logger.info("Based on dataset characteristics, Max Sequence Length = {}".format(max_seq_length))

    return max_seq_length
