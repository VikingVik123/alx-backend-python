#!/usr/bin/env python3
"""
Function to satisfy task 7
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    k: str to display
    v: float and int list
    """
    return (k, float(v ** 2))

