from math import sqrt


# This is simple function used as sequence producer
def lucas():
    yield 2
    a, b = 2, 1
    while True:
        yield b
        a, b = b, a + b


# 1) Just regular function: directly returns the result or raises an exception
def search(iterable, predicate):
    for item in iterable:
        if predicate(item):
            return item
    raise ValueError("Not Found")


search(lucas(), lambda x: len(str(x)) >= 6)
# >>> 103682


# 2) Periodically yields control to scheduler (on every iteration)
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

# ....... go to the 'scheduler.py' here


# 8) Create long-running function with CPU-bounded calculation
def is_prime(x):
    """Pretty ineffective function"""
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

# 9) Try to get cooperative execution of two functions

# scheduler = Scheduler()
# scheduler.add(
#     async_repetitive_message_first("A Loud Automatic Repetitive Message", 2.5)
# )
# scheduler.add(async_print_matches(lucas(), is_prime))
# scheduler.run_to_completion()

# But we failed.
# The reason is that "is_prime" function is blocking, it doesn't return control
