#!/usr/bin/env python3
"""Concurrent corutines"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Async function that calls another"""
    val = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    for i in range(len(val)):
        for j in range(i + 1, len(val)):
            if val[i] > val[j]:
                val[i], val[j] = val[j], val[i]
    return val
