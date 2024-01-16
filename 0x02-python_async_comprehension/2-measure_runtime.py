#!/usr/bin/env python3
"""func to measure the execution time."""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """func to measure the execution time."""
    st = time.perf_counter()

    tk = [async_comprehension() for x in range(4)]
    await asyncio.gather(*tk)

    ed = time.perf_counter()

    return (ed - st)
