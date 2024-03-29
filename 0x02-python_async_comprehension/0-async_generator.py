#!/usr/bin/env python3

"""
Async Generator module
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random numbers between 0 and 10.
    This coroutine loops 10 times, asynchronously waiting 1 second each time.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
