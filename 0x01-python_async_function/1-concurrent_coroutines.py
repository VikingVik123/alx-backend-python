#!/usr/bin/env python3
"""
Code to return a list of tasks
"""
import asyncio
import importlib
from typing import List


wait_random_module = importlib.import_module("0-basic_async_syntax")
wait_random = wait_random_module.wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Initializes wait_n function task
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
