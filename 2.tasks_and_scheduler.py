from collections import deque


# 3) Define simple coroutine/generator wrapper (keep track of 'id' as well)
class Task:
    next_id = 0

    def __init__(self, routine):
        self.id = self.__class__.next_id
        self.__class__.next_id += 1
        self.routine = routine
