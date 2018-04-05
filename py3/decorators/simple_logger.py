def logger(fn):
    def wrapped(*args, **kwargs):
        print('This has been logged')
        fn(*args, **kwargs)
        print('This has been logged afterwards')
    return wrapped


@logger
def my_func(num1, num2):
    print(f'{ num1 + num2 }')


my_func(10, 20)
