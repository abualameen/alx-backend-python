#!/usr/bin/env python3
"""
This module defines a function to zoom in on an array by
repeating each element.
"""


from typing import Tuple, List, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    """
    Zooms in on an array by repeating each element.

    Args:
        lst (Tuple[Any, ...]): The input array.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        Tuple[Any, ...]: The zoomed-in array.
    """
    zoomed_in = tuple(item for item in lst for _ in range(factor))
    return zoomed_in
