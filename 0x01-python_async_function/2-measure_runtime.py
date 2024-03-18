#!/usr/bin/env python3

"""
Measure runtime module
"""

import asyncio
import time
from typing import Callable


# Importing wait_n function from previous script
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return the average time per call.
    Args:
        n (int): Number of times to call wait_n.
        max_delay (int): Maximum delay for each wait_n call.
    Returns:
        float: Average time per call.
    """
    # Start measuring time
    start_time = time.time()

    # Call wait_n function
    asyncio.run(wait_n(n, max_delay))

    # Calculate total time elapsed
    total_time = time.time() - start_time

    # Return average time per call
    return total_time / n
