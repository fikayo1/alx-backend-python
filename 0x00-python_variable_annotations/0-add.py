#!/usr/bin/env python3
""" Type annotated function to add"""

def add(a: float, b:float) -> float:
    """ Function to return sum of a and B"""
    return a+b

print(add(2, 5.0))