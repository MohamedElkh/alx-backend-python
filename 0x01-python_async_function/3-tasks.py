#!/usr/bin/env python3
"""func to contain a method to return tasks"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """func to return the waited from random num of sec"""
    return asyncio.create_task(wait_random(max_delay))
