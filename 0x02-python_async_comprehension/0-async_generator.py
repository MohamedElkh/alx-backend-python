#!/usr/bin/env python3
"""this model py to loop for 10 times"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """func async_generator to loop 10 times"""
    for x in range(10):
        await asyncio.sleep(1)

        yield random.uniform(0, 10)
