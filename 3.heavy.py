from math import sqrt


def is_prime(x):
    """Pretty uneffective 'is_prime' function"""
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def async_print_matches(iterable, predicate):
    for item in iterable:
        if predicate(item):
            print('Found: ', item, end=', ')
        yield


