def mapper(fn, items):
    res = []
    for item in items:
        res.append(fn(item))
        yield
    return res


def runner(gen):
    while True:
        try:
            next(gen)
        except StopIteration as e:
            return e.value
