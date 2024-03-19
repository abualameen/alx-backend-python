#!/usr/bin/env python3

"""
Async Generator module that yields random numbers between 0 and 10 with a one-second delay.
"""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields random numbers between 0 and 10.
    This coroutine loops 10 times, asynchronously waiting 1 second each time.
    Raises:
        asyncio.TimeoutError: If the coroutine takes longer than expected to complete.
    Returns:
        AsyncGenerator[float, None]: An asynchronous generator yielding random numbers.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
