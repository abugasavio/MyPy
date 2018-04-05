def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


assert factorial(10) == 3628800
