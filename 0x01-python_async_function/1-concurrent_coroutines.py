#!/usr/bin/env python3
"""func to contain the method wait random n times"""
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """func to contain the method wait random n times"""
    tks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    return [await tk for tk in asyncio.as_completed(tks)]
