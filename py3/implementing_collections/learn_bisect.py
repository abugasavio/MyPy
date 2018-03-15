import bisect
import random

random.seed(1)

l = []
for i in range(1, 20):
    r = random.randint(1, 100)
    position = bisect.bisect(l, r)
    bisect.insort(l, r)
    print('{} {}'.format(r, position), end='')
    print(l)
