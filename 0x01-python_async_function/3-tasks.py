#!/usr/bin/env python3
"""Task 3"""
import asyncio
from typing import Coroutine

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Coroutine:
    """Returns a coroutine object that waits for a random amount of time.

    Args:
        max_delay (int): The maximum amount of time to wait, in seconds.

    Returns:
        Coroutine: A coroutine object that waits for a random amount of time.
    """
    # Create a task that will wait for a random amount of time
    # using the `wait_random` coroutine function.
    return asyncio.create_task(wait_random(max_delay))
