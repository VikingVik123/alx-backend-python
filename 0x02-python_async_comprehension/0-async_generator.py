#!/usr/bin/env python3
"""
Code to create an async generator
Returns a list of values
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, NoneType, NoneType]:
    """
    initializes async_generation function
    numbers: stores the random numbers generated
    """
    numbers = random.uniform(0, 10)
    for _ in range(10):
        await asyncio.sleep(1)

        yield numbers
