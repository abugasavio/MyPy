import time


def timer(fn):
    def wrapped(*args, **kwargs):
        t1 = time.time()
        fn(*args, **kwargs)
        t2 = time.time()
        return 'time it took {}'.format(str(t2 - t1))
    return wrapped


def fib(n):
    print("Calculating F", "(", n, ")", sep="", end=", ")
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(5))
