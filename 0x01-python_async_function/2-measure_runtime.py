#!/usr/bin/env python3
"""this func to contain method to measure total exec time"""
import asyncio
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """func to measure total exe time in func"""
    st = perf_counter()

    asyncio.run(wait_n(n, max_delay))
    exit = perf_counter() - st

    return exit / n
