def chain(x, y):
    yield from x
    yield from y


x = [1, 2, 3]
y = [4, 5, 6]

