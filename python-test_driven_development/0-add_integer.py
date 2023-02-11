#!/usr/bin/python3
"""Function that adds 2 integers"""


def add_integer(a, b=98):
    """Add 2 integers"""
    try:
        return(int(a + b))
    except TypeError:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        elif not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")
