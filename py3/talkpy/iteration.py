
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, it):
        self.items.append(it)

    def __iter__(self):
        sorted_items = sorted(self.items, key=lambda i: -i.price)
        # return sorted_items.__iter__()


class CartItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = ShoppingCart()
cart.add_item(CartItem("Guitar", 599))
cart.add_item(CartItem("CD", 19))
cart.add_item(CartItem("iPhone", 599))

for item in cart:
    print("* - {} ${}".format(item.name, item.price))
