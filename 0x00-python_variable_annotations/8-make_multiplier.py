#!/usr/bin/env python3
"""This module contain the make multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a multiplier function"""
    def func(number):
        return multiplier * number
    return func
