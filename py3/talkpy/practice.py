# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.


def numbers():
    for number in range(2000, 3200):
        if number % 7 == 0 and number % 5 != 0:
            yield number


print(list(numbers()))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(8))
