#!/usr/bin/env python3

"""
function to return a function
""" 
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function

