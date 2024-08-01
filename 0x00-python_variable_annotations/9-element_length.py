#!/usr/bin/env python3
"""
Function to determine length
"""
from typing import List, Tuple, Any


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    initialization
    """
    return [(i, len(i)) for i in lst]
