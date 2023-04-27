#!/usr/bin/env python3
"""This module contain the tokv function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return params as a tuple"""
    return (k, v ** 2)
