import time


# 5) Create function that print a message and sleeps actually for some time
def repetitive_message(message, interval_seconds):
    while True:
        print(message)
        start = time.time()
        expiry = start + interval_seconds
        while True:
            now = time.time()
            if now >= expiry:
                break


# 6) Refactor that to make it cooperative (return control)
def bug_async_repetitive_message(message, interval_seconds):
    """Yields control until time interval expires"""
    while True:
        print(message)
        start = time.time()
        expiry = start + interval_seconds
        while True:
            now = time.time()
            if now >= expiry:
                break
            yield

# BUT if 'interval_seconds' in 'bug_async_repetitive_message' is 0,
# coroutine will never yield (will never be reached) and will hog the system


# 7) Finish refactoring and ensure that
# coroutines always yield AT LEAST ONCE if they can't complete immediately
def async_repetitive_message(message, interval_seconds):
    """Yields control until time interval expires"""
    while True:
        print(message)
        start = time.time()
        expiry = start + interval_seconds
        while True:
            yield
            now = time.time()
            if now >= expiry:
                break
