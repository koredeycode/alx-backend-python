#!/usr/bin/env python3
"""
documentation for this module
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
        The function documentation
    """
    i: float = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
