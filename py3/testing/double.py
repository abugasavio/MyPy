import sys

def doubleit(x):
    if not isinstance(x, (int, float)):
        raise TypeError
    return x * 2

if __name__ == '__main__':
    number = sys.argv[1]
    double_val = doubleit(number)
    print("the value of {} is {}".format(number, double_val))


