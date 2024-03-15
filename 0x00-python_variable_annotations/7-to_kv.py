#!/usr/bin/env python3
"""
This module defines a function to create a tuple
from a string and the square of an int or float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple from a string and the square of an int or float.

    Args:
        k (str): The string.
        v (Union[int, float]): The int or float.

    Returns:
        Tuple[str, float]: A tuple containing the string k and the square of v.
    """
    return (k, v * v)
