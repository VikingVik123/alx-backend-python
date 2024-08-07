#!/usr/bin/env python3
"""
write a function measure_runtime coroutine
To execute async_comprehension four times in parallel
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Function initialization
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    diff = end_time - start_time

    return diff
