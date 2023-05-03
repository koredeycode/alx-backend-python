#!/usr/bin/env python3

"""
Module documentation
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Generate a sequence of 10 numbers
    """
    result = [i async for i in async_generator()]
    return result
