def fibonacci():
    current, nxt = 0, 1
    while True:
        yield current
        current, nxt = nxt, current + nxt


for number in fibonacci():
    print(number)
