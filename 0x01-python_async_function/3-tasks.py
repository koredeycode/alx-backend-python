#!/usr/bin/env python3
"""
documentation for this module
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
        Function documentation
    """
    return asyncio.Task(wait_random(max_delay))
