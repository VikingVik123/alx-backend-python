#!/usr/bin/env python3
"""
Code to create an async generator
Returns a list of values
"""
import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """
    initializes async_generation function
    numbers: stores the random numbers generated
    """
    numbers = random.uniform(0, 10)
    for _ in range(10):
        await asyncio.sleep(1)
        yield numbers