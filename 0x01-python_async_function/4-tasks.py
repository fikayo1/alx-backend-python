#!/usr/bin/env python3
"""Async functions"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Async function that calls another"""
    tasks = [task_wait_random(max_delay) for i in range(n)]
    val = await asyncio.gather(*tasks)
    for i in range(len(val)):
        for j in range(i + 1, len(val)):
            if val[i] > val[j]:
                val[i], val[j] = val[j], val[i]
    return val
