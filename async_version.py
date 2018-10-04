import time
from math import sqrt


def async_is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
        yield
    return True


def async_print_matches(iterable, async_predicate):
    for item in iterable:
        # allow the predicate to make progress and yield control
        matches = yield from async_predicate(item)
        if matches:
            print('Found: ', item, end=', ')
        # yield at the end is no needed, we yielding from 'inner' coroutine


def async_sleep(interval_seconds):
    # Always yields at least once.
    # P.S.: ```async_sleep(0)``` yields exactly once
    # PP.S: 'bare yield' can be replaced with ```yield from async_sleep(0)```
    # and only that function could contain 'bare yield'
    start = time.time()
    expiry = start + interval_seconds
    while True:
        yield
        now = time.time()
        if now >= expiry:
            break
