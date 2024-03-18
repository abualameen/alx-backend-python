#!/usr/bin/env python3

"""
Tasks module
"""

import asyncio
from typing import List  # Importing List type hint

# Importing task_wait_random from 3-tasks using the specified import syntax
task_wait_random = __import__(
                                '3-tasks',
                                fromlist=['task_wait_random']
                                ).task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns task_wait_random n times
    with the specified max_delay and returns the list of delays
    in ascending order.
    Args:
        n (int): Number of times to call task_wait_random.
        max_delay (int): Maximum delay for each task_wait_random call.
    Returns:
        List[float]: List of delays in ascending order.
    """
    # List to store delays
    delays = []

    # Create tasks for task_wait_random and collect the results
    for _ in range(n):
        delay = await task_wait_random(max_delay)
        delays.append(delay)

    # Sort the delays in ascending order
    delays.sort()

    return delays
