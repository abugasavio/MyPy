def countdown(count_to):
    while count_to:
        yield count_to
        count_to -= 1


tasks = [countdown(10), countdown(5), countdown(20)]


while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:
        print('Task finished')
