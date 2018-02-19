def hypervolume(length, *lengths):
    v = length
    for length in lengths:
        v *= length
    return v


print(hypervolume(4,2, 5))
