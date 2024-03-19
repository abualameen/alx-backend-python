import asyncio

# Import the async_generator
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> list[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension over async_generator.
    Returns:
        List[float]: List of 10 random numbers.
    """
    # Collect 10 random numbers using async comprehension
    random_numbers = [random_number async for random_number in async_generator()]
    return random_numbers
