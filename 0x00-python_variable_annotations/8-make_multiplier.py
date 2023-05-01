#!/usr/bin/env python3
""" Multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float"""
    def f(n):
        """Multiply n by multiplier"""
        return n * multiplier
    return f
