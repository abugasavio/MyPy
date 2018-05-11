from collections import deque
from types import coroutine

friends = deque(('Joseph', 'Mark', 'Anthony'))


@coroutine
def friends_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(g):
    await g


gen = greet(friends_upper())

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
