


def foo(*args, name='Sam') -> int:
    print(args)
    print(f'Hello, {name}')
    return 2.0


foo()
foo('matt')
