from collections import deque


# 3) Define simple coroutine/generator wrapper (keep track of 'id' as well)
class Task:
    next_id = 0

    def __init__(self, routine):
        self.id = self.__class__.next_id
        self.__class__.next_id += 1
        self.routine = routine


# 4) Define simple scheduler
class Scheduler:
    def __init__(self):
        self.runnable_tasks = deque()
        self.completed_tasks_results = {}
        self.failed_tasks_errors = {}

    def add(self, routine):
        task = Task(routine)
        self.runnable_tasks.append(task)
        return task.id

    def run_to_completion(self):
        while self.runnable_tasks:
            task = self.runnable_tasks.popleft()
            print('Running task {} ...'.format(task.id), end='')
            try:
                yielded = next(task.routine)
            except StopIteration as stopped:  # task is finished, collect result
                value = stopped.value
                print('Completed with result: {}'.format(value))
                self.completed_tasks_results[task.id] = value
            except Exception as e:
                print('Failed with exception: {}'.format(e))
                self.failed_tasks_errors[task.id] = e
            else:
                assert yielded is None  # yielded was successful
                print('now yielded')
                self.runnable_tasks.append(task)  # add to the back of queue
