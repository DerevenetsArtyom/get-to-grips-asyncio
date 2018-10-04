import time
from math import sqrt
from scheduler import Scheduler
from main import lucas


def async_is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
        yield  # could be ```yield from async_sleep(0)```
    return True


def async_print_matches(iterable, async_predicate):
    for item in iterable:
        # allow the predicate to make progress and yield control
        matches = yield from async_predicate(item)
        if matches:
            print('Found: ', item)
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


# 10) Refactoring using async_sleep()
def async_repetitive_message(message, interval_seconds):
    """Yields control until time interval expires"""
    while True:
        print(message)
        yield from async_sleep(interval_seconds)


# 11) Try one more time to get cooperative execution of two functions
# now this non-blocking 'async_is_prime' that was an issue lat time.
if __name__ == '__main__':
    scheduler = Scheduler()
    scheduler.add(
        async_repetitive_message("A Loud Automatic Repetitive Message", 2.5)
    )
    scheduler.add(async_print_matches(lucas(), async_is_prime))
    # NB: prints inside "run_to_completion" should be disabled
    scheduler.run_to_completion()
    # >>> A Loud Automatic Repetitive Message
    # >>> Found:  2
    # >>> Found:  3
    # >>> Found:  7
    # >>> Found:  11
    # >>> Found:  29
    # >>> Found:  47
    # >>> Found:  199
    # >>> Found:  521
    # >>> Found:  2207
    # >>> Found:  3571
    # >>> Found:  9349
    # >>> Found:  3010349
    # >>> Found:  54018521
    # >>> Found:  370248451
    # >>> Found:  6643838879
    # >>> Found:  119218851371
    # >>> A Loud Automatic Repetitive Message
    # >>> Found:  5600748293801
    # >>> A Loud Automatic Repetitive Message
    # >>> A Loud Automatic Repetitive Message

