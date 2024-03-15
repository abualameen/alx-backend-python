#!/usr/bin/env python3
"""
This module defines a function to safely get a value from a dictionary.
"""


from typing import Mapping, Any, TypeVar, Union


# Define a generic type variable for the value returned by the function
T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary, returning a default
    value if the key is not found.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to search for in the dictionary.
        default (Union[T, None], optional): The default value to
        return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value corresponding to the key in the
        dictionary, or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
