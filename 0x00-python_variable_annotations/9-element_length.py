#!/usr/bin/env python3
"""
This module defines a function to calculate the length of
elements in an iterable.
"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing elements from the input
    list along with their lengths.

    Args:
        lst (Iterable[Sequence]): An iterable object containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each
        tuple contains an element from lst and its length.
    """
    return [(i, len(i)) for i in lst]
