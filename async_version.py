from main import lucas, is_prime
from repetitive_message_evolution import async_repetitive_message
from scheduler import Scheduler


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

