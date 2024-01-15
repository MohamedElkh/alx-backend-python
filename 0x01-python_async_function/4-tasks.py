#!/usr/bin/env python3
"""func to contain method to spwans tasks n times"""
from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """func to spawn task_wait_random n times with spec delay"""
    tks = [task_wait_random(max_delay) for _ in range(n)]

    return [await tk for tk in asyncio.as_completed(tks)]
