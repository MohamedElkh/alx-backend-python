#!/usr/bin/env python3
"""this func contain the delays of certain amount of time"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """this func return he float from 0 to max"""
    rd = random.uniform(0, max_delay)

    await asyncio.sleep(rd)
    return rd
