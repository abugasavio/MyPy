from collections import deque


class Task:
    id = 1

    def __init__(self, gen):
        self.task_id = Task.id
        Task.id += 1
        self.gen = gen


class Scheduler:
    def __init__(self):
        self.tasks = deque()
        self.results = {}
        self.exceptions = {}

    def add(self, gen):
        self.tasks.append(Task(gen))

    def run(self):
        while True:
            if not self.tasks:
                break
            task = self.tasks.popleft()
            try:
                print(f'Run: {task.task_id}')
                next(task.gen)
            except StopIteration as e:
                self.results[task.task_id] = e.value
                print(f'Results: {self.results}')
            except Exception as e:
                self.exceptions[task.task_id] = e
            else:
                self.tasks.append(task)
