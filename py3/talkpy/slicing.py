def fib(limit):
    numbers = []
    current, nxt = 0, 1
    while current < limit:
        current, nxt = nxt, nxt + current
        numbers.append(current)
