from collections import deque
from types import coroutine


friends = deque(('Rolf', 'Jose', 'Charlie'))


@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(g):
    await g


greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
