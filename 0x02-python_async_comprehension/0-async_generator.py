#!/usr/bin/env python3
"""Aync generator"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Loops 10 times and returns a random number"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
