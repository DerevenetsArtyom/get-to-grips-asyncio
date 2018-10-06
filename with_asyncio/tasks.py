import asyncio
from asyncio import ensure_future
from main import lucas, is_prime, search
from futures import twelve_digits_prime, monitor_future

# TASK - a subclass of Future which wraps a coroutine (wtf?)
# Task is-a Future
# Task has/contains a coroutine

# #1. Version with 'create_task' function

# loop = asyncio.get_event_loop()
# co_obj = search(lucas(), twelve_digits_prime)
# search_task = loop.create_task(co_obj)
# loop.create_task(monitor_future(search_task, 1))
# loop.run_until_complete(search_task)
# print(search_task.result())
# loop.close()

# #2. Version with 'ensure_future' function
if __name__ == '__main__':
    search_task = ensure_future(search(lucas(), twelve_digits_prime))
    monitor_task = ensure_future(monitor_future(search_task, 1))

    search_and_monitor_future = asyncio.gather(search_task, monitor_task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(search_and_monitor_future)
    print(search_task.result())
    loop.close()
