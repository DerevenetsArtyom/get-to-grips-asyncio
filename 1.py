def lucas():
    yield 2
    a, b = 2, 1
    while True:
        yield b
        a, b = b, a + b


def search(iterable, predicate):
    for item in iterable:
        if predicate(item):
            return item
    raise ValueError("Not Found")


print(search(lucas(), lambda x: len(str(x)) >= 6))
