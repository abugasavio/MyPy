from collections import deque

def greet():
    friend = yield
    print(f'Hello, {friend}')


# g = greet()
# g.send(None)  # priming
# g.send('Savio')


friends = deque(('Rolf', 'Jose', 'Charlie'))


def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


def greet(g):
    g.send(None)  # priming
    while True:
        greeting = yield
        g.send(greeting)


greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
