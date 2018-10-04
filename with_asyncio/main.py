from math import sqrt
import time


def lucas():
    yield 2
    a, b = 2, 1
    while True:
        yield b
        a, b = b, a + b


def async_search(iterable, predicate):
    for item in iterable:
        if predicate(item):
            return item
        yield from async_sleep(0)
    raise ValueError("Not Found")


def async_is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
        yield from async_sleep(0)
    return True


def async_print_matches(iterable, async_predicate):
    for item in iterable:
        # allow the predicate to make progress and yield control
        matches = yield from async_predicate(item)
        if matches:
            print('Found: ', item)


def async_sleep(interval_seconds):
    start = time.time()
    expiry = start + interval_seconds
    while True:
        yield
        now = time.time()
        if now >= expiry:
            break


def async_repetitive_message(message, interval_seconds):
    while True:
        print(message)
        yield from async_sleep(interval_seconds)
