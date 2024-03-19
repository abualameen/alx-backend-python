"""
this module implements async comprehension

"""

import asyncio
from typing import List
from time import time

# Import async_comprehension from the previous file
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine to measure the total runtime for executing
    async_comprehension four times in parallel.
    Returns:
        float: Total runtime in seconds.
    """
    # Start measuring time
    start_time = time()

    # Execute async_comprehension four times in parallel using asyncio.gather
    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    # Calculate total runtime
    total_runtime = time() - start_time

    return total_runtime

if __name__ == "__main__":
    # Run the main coroutine and print the total runtime
    print(asyncio.run(measure_runtime()))
