#!/usr/bin/env python3
"""Measure runtime."""
import time
from asyncio import gather

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Return the runtime of 4 concurrent async comprehensions."""
    start = time.perf_counter()
    await gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    return (time.perf_counter() - start)
