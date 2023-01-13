import asyncio
import time

async def print_something(delay, word):
    print(f"Before {word}")
    await asyncio.sleep(delay)
    print(f"After {word}")

async def main():
    t = time.time()
    print("Start")
    task1 = asyncio.create_task(print_something(2, "Task 1"))
    task2 = asyncio.create_task(print_something(2, "Task 2"))
    await task1
    await task2
    print("Finished: {}s".format(time.time()-t))

asyncio.run(main())