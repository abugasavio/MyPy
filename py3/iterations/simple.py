class ExampleIterator:
    def __init__(self, items):
        self.index = 0
        self.items = items

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.items) - 1:
            raise StopIteration('End')
        else:
            i = self.index
            self.index += 1
            return self.items[i]
