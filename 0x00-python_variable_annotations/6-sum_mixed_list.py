#!/usr/bin/env python3
"""
Func to add a list of mixed num values
"""
import math
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    initalized fxn to add values of mxd_lst
    """
    return (math.fsum(mxd_lst))

