#!/usr/bin/env python3
"""
Function 2 return sum of values in a list
"""
import math
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    input_list: list to sum and return the values of
    """
    return(float(math.fsum(input_list)))

