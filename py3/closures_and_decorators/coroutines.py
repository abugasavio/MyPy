import time
from math import sqrt
from collections import deque
from itertools import islice


def async_is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
        yield from async_sleep(0)
    return True


def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b


def async_search(iterable, predicate):
    for item in iterable:
        if predicate(item):
            return item
        yield from async_sleep(0)
    raise ValueError("Not Found")


def async_sleep(interval_seconds):
    start = time.time()
    expiry = start + interval_seconds
    while True:
        yield
        now = time.time()
        if now >= expiry:
            break


def async_repetitive_message(message, interval_seconds):
    while True:
        print(message)
        yield from async_sleep(interval_seconds)


def async_print_matches(iterable, async_predicate):
    for item in iterable:
        matches = yield from async_predicate(item)
        if matches:
            print(f"Found {item}", end=", ")


g = async_search(lucas(), lambda x: x >= 10)


class Task:
    next_id = 0

    def __init__(self, routine):
        self.id = Task.next_id
        Task.next_id += 1
        self.routine = routine


class Scheduler:
    def __init__(self):
        self.runable_tasks = deque()
        self.completed_task_results = {}
        self.failed_task_errors = {}

    def add(self, routine):
        task = Task(routine)
        self.runable_tasks.append(task)
        return task.id

    def run_to_completion(self):
        while len(self.runable_tasks) != 0:
            task = self.runable_tasks.popleft()
            print(f'Running task  {task.id}', end='')
            try:
                yielded = next(task.routine)
            except StopIteration as stopped:
                print('completed with task{!r}'.format(stopped.value))
                self.completed_task_results[task.id] = stopped.value
            except Exception as e:
                print('Failed with exception: {}'.format(e))
            else:
                assert yielded is None
                print("Now yielded")
                self.runable_tasks.append(task)
