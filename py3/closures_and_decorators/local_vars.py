def raise_to(power):
    mini = 20

    def raiser(number):
        mini
        return pow(number, power)
    return raiser


square = raise_to(2)
print(f'{square.__closure__}')
