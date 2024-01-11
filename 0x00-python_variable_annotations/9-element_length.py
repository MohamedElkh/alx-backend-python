#!/usr/bin/env python3
"""func with annotated parameters return values"""
from typing import Tuple, Sequence, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """func to return the list of tuples"""
    return [(i, len(i)) for i in lst]
