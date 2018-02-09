def outer_func(message):
    def inner_func():
        print(message)
    return inner_func


func = outer_func('Hi there')
print(func())
