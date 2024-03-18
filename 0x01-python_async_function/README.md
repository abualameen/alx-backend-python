# Asynchronous Python Programming with asyncio

This repository contains Python scripts demonstrating the basics of asynchronous programming using asyncio. Asynchronous programming allows you to perform multiple tasks concurrently, improving performance and efficiency, especially in I/O-bound operations.

## Async and Await Syntax

Python's `async` and `await` keywords are used to define asynchronous functions and manage asynchronous operations. 

- `async`: It defines a function as a coroutine, indicating that it can be paused and resumed.
- `await`: It is used within an `async` function to pause the execution until an asynchronous operation is completed.

## Executing an Async Program with asyncio

The `asyncio` module in Python provides infrastructure for writing single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources.

To execute an async program with asyncio:
1. Define async functions using the `async def` syntax.
2. Use `asyncio.run()` to run the main async function.

## Running Concurrent Coroutines

Concurrent coroutines can be run either using `asyncio.gather()` or `asyncio.create_task()`.

- `asyncio.gather()`: Allows you to run multiple coroutines concurrently and wait for all of them to complete.
- `asyncio.create_task()`: Creates a task for a coroutine and schedules it to run concurrently.

## Creating asyncio Tasks

Asyncio tasks can be created using `asyncio.create_task()` or by wrapping coroutine in `asyncio.Task()`.

Asyncio tasks allow you to schedule and manage the execution of coroutines concurrently.

## Using the Random Module

The `random` module in Python provides functions to generate random numbers, which can be useful for various purposes, such as generating random data or shuffling sequences.

To use the random module:
1. Import the `random` module.
2. Use functions like `random.randint()` to generate random integers or `random.shuffle()` to shuffle sequences.

## Scripts

- `0-basic_async_syntax.py`: Contains an asynchronous coroutine `wait_random()` that waits for a random delay between 0 and a specified maximum delay (default 10) seconds and returns it.
- `0-main.py`: Test script for `wait_random()` coroutine.

## How to Run

To execute the scripts:
1. Ensure you have Python 3.7 or later installed.
2. Navigate to the directory containing the scripts.
3. Run the desired script using the Python interpreter.
