#!/usr/bin/env python3
"""
Create a measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. Your function should return a float.

Use the time module to measure an approximate elapsed time.
"""
import asyncio
import importlib
import time


concurrent_coroutines = importlib.import_module("1-concurrent_coroutines")
wait_n = concurrent_coroutines.wait_n

async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per task.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
