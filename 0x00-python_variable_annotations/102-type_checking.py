#!/usr/bin/env python3
"""
This module defines a function to zoom in on an array by
repeating each element.
"""


from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on an array by repeating each element.

    Args:
        lst (Tuple): The input array.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        List: The zoomed-in array.
    """
    zoomed_in = [item for item in lst for _ in range(factor)]
    return zoomed_in
