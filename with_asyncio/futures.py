import asyncio
from main import lucas, is_prime, search

# FUTURE - encapsulates a potential result or error


async def ten_digits_prime(x):
    return (await is_prime(x)) and len(str(x)) == 10


async def monitored_search(iterable, predicate, future):
    try:
        found_item = await search(iterable, predicate)
    except ValueError as not_found:
        future.set_exeption(not_found)
    else:  # no exception
        future.set_result(found_item)


async def monitor_future(future, interval_seconds):
    while not future.done():
        print('Waiting...')
        await asyncio.sleep(interval_seconds)
    print('Done!')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    future = loop.create_future()
    co_obj = monitored_search(lucas(), ten_digits_prime, future)
    loop.create_task(co_obj)
    loop.create_task(monitor_future(future, 1))
    loop.run_until_complete(future)
    print(future.result())
    loop.close()
