#!/usr/bin/env python3
"""func to contains metoid safely gets value from dictionary"""
from typing import Union, Any, Mapping, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """func to Safely gets value from dictionary."""
    if key in dct:
        return dct[key]
    else:
        return default
