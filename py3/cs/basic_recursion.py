def basic_recursion(max, current):
    print(max, current)
    if current > max:
        return
    else:
        basic_recursion(max, current + 1)


basic_recursion(5, 1)
