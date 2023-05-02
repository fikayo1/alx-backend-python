#!/usr/bin/env python3
"""Basic async"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Asynchronuc function that waits"""
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
