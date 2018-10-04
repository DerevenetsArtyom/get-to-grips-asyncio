import asyncio
from math import sqrt


def lucas():
    yield 2
    a, b = 2, 1
    while True:
        yield b
        a, b = b, a + b


async def search(iterable, predicate):
    for item in iterable:
        if predicate(item):
            return item
        await asyncio.sleep(0)
    raise ValueError("Not Found")


async def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
        await asyncio.sleep(0)
    return True


async def print_matches(iterable, async_predicate):
    for item in iterable:
        # allow the predicate to make progress and yield control
        matches = await async_predicate(item)
        if matches:
            print('Found: ', item)


async def repetitive_message(message, interval_seconds):
    while True:
        print(message)
        await asyncio.sleep(interval_seconds)

if __name__ == '__main__':
    scheduler = asyncio.get_event_loop()  # instead of old Scheduler()
    scheduler.create_task(  # instead of old .add()
        repetitive_message("A Loud Automatic Repetitive Message", 2.5)
    )
    scheduler.create_task(print_matches(lucas(), is_prime))
    scheduler.run_forever()  # instead of old .run_to_completion()
