# This is example function used as sequence producer
def lucas():
    yield 2
    a, b = 2, 1
    while True:
        yield b
        a, b = b, a + b


# Regular function: directly returns the result or raises an exception
def search(iterable, predicate):
    for item in iterable:
        if predicate(item):
            return item
    raise ValueError("Not Found")


search(lucas(), lambda x: len(str(x)) >= 6)
# >>> 103682


def async_search(iterable, predicate):
    for item in iterable:
        if predicate(item):
            return item
        yield
    raise ValueError("Not Found")
