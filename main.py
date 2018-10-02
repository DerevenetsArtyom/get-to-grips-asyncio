from math import sqrt


# This is example function used as sequence producer
def lucas():
    yield 2
    a, b = 2, 1
    while True:
        yield b
        a, b = b, a + b


# 1) Regular function: directly returns the result or raises an exception
def search(iterable, predicate):
    for item in iterable:
        if predicate(item):
            return item
    raise ValueError("Not Found")


search(lucas(), lambda x: len(str(x)) >= 6)
# >>> 103682


# 2) Periodically yields control to scheduler
def async_search(iterable, predicate):
    for item in iterable:
        if predicate(item):
            return item
        yield
    raise ValueError("Not Found")


g = async_search(lucas(), lambda x: x >= 10)
# <generator object async_search at 0x7f2b4aac8200>
# actually encapsulate code and state of that code / function
# >>> next(g)


# .......

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
