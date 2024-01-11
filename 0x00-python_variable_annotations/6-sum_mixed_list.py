#!/usr/bin/env python3
"""func takes mixed lists of ints and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """this func takes lists of ints and floats"""
    return sum(mxd_lst)
