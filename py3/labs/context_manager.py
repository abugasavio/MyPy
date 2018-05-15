class runner:
    def __init__(self, item):
        self.item = item
        item

    def __enter__(self):
        self.item['running'] = True

    def __exit__(self, ex, val, tab):
        self.item['running'] = False


item: dict = {}

with runner(item):
    print(item['running'])

print(item['running'])
