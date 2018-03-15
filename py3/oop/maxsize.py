class MaxSizeList:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self._items = []

    def push(self, item):
        if len(self._items) < self.maxsize:
            self._items.append(item)
        else:
            self._items.pop(0)
            self._items.append(item)

    def get_list(self):
        return self._items
