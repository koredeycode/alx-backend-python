#!/usr/bin/env python3
"""
documentation for this module
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        The function documentation
    """
    res = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    return res
