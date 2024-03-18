#!/usr/bin/env python3

"""
Tasks module
"""

import asyncio

# Importing wait_random from 0-basic_async_syntax
# using the specified import syntax
wait_random = __import__(
                        '0-basic_async_syntax',
                        fromlist=['wait_random']).wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function that takes an integer max_delay
    and returns an asyncio.Task.
    Args:
        max_delay (int): Maximum delay for wait_random.
    Returns:
        asyncio.Task: Task for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
