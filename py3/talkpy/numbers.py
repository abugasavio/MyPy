

def number(i):

    while i > 0:
        yield i % 10
        i //= 10
