#!/usr/bin/env python3
"""
Function to determine length
"""
from typing import List, Tuple, Any


def element_length(lst: List[Any]) -> List[Tuple[Any, int]]:
    """
    initialization
    """
    return [(i, len(i)) for i in lst]
