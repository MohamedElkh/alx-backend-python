#!/usr/bin/env python3
"""func to return a list of int multi by certain factor"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """func to return the list of ints multiplied by certain factor"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
