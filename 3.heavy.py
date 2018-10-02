import time


# 5) Create function that print a message and sleeps actually for some time
def repetitive_message(message, interval_seconds):
    """Yields control until time interval expires"""
    while True:
        print(message)
        start = time.time()
        expiry = start + interval_seconds
        while True:
            now = time.time()
            if now >= expiry:
                break