def divisor(number):
    for i in range(2, number):
        if number % i == 0:
            yield i


print(list(divisor(12099070470612436127436218687678)))
