#!/usr/bin/env python3

"""
Concurrent coroutines module
"""

import asyncio
from typing import List

# Importing wait_random coroutine from previous script
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times
    with the specified max_delay and returns the list of delays
    in ascending order.
    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay for each wait_random call.
    Returns:
        List[float]: List of delays in ascending order.
    """
    # List to store delays
    delays = []

    # Create tasks for wait_random and collect the results
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    # Sort the delays in ascending order
    delays.sort()

    return delays
