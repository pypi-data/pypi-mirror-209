# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2022 Baidu.com, Inc. All Rights Reserved
"""
triton client utils
"""
import uuid

import numpy as np


def gen_unique_id():
    """
    Generate unique id
    """
    return str(uuid.uuid4().hex)


def list_stack_ndarray(arrays) -> np.ndarray:
    """
    Convert list of ndarrays to single ndarray with ndims+=1
    """
    lengths = list(
        map(lambda x, a=arrays: a[x].shape[0], [x for x in range(len(arrays))])
    )
    max_len = max(lengths)
    arrays = list(map(lambda a, ml=max_len: np.pad(a, (0, ml - a.shape[0])), arrays))
    for arr in arrays:
        assert arr.shape == arrays[0].shape, "arrays must have the same shape"
    return np.stack(arrays, axis=0)


def parse_model(model_metadata, model_config):
    """
    Check the configuration of a model to make sure it meets the
    requirements for an image classification network (as expected by
    this client)
    """
    input_metadata = model_metadata['inputs']
    output_metadata = model_metadata['outputs']

    max_batch_size = None
    if "max_batch_size" in model_config:
        max_batch_size = model_config['max_batch_size']

    return input_metadata, output_metadata, max_batch_size
