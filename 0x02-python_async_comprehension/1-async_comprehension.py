#!/usr/bin/env python3
"""
Import async_generator from the previous task
write a coroutine called async_comprehension that takes no arguments
"""
import asyncio
import random
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    initializes function
    """
    return [number async for number in async_generator()]
