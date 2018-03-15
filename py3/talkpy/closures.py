def outer_func(message):
    """
    outer_func returns a closure function
    :param message: Some message
    :return: cl
    """
    def inner_func():
        print(message)

    return inner_func


func = outer_func()
print(func())
