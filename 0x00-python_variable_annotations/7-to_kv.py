#!/usr/bin/env python3
"""func to convert pythong to kv pair"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """func to convert pythong to kv pair"""
    return k, v ** 2
