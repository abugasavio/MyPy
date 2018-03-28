curr = 1
accum = 0


def recursive_sum():
    global curr
    global accum

    print("current: {}".format(curr))
    print("accumulated: {}".format(accum))
    if curr == 11:
        return accum
    else:
        accum = curr + accum
        curr = curr + 1
        return recursive_sum()


print(recursive_sum())
