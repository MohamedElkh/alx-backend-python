#!/usr/bin/env python3
"""func that multi floats by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """func to multi a float by multi"""
    def func_multi(num: float) -> float:
        """func to Multiplies a float"""
        return multiplier * num

    return func_multi
