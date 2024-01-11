#!/usr/bin/env python3
"""func that sums a list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """func to sums a list of float"""
    if input_list is None:
        return 0
    else:
        return sum(input_list)
