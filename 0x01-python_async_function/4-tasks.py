#!/usr/bin/env python3
"""
documentation for this module
"""
import asyncio
from typing import List
twr = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        function documentation
    """
    res = await asyncio.gather(*[twr(max_delay) for _ in range(n)])
    return sorted(res)
