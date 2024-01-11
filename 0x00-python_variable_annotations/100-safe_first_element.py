#!/usr/bin/env python3
"""func to Augmented code with the correct duck-typed"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """func to return the first elem of list or none"""
    if lst:
        return lst[0]
    else:
        return None
