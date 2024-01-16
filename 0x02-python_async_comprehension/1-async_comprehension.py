#!/usr/bin/env python3
"""python func to returns 10 random numbers using async"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """func to returns 10 random numbers using async"""
    rsx = [x async for x in async_generator()]

    return rsx
