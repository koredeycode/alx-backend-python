#!/usr/bin/env python3

"""
Module documentation
"""
import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """
    Generate a sequence of 10 numbers
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
