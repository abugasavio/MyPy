class MaxSizeList:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self._items = []

    def push(self, item):
        self._items.append(item)
        if len(self._items) > self.maxsize:
            self._items.pop(0)

    def get_list(self):
        return self._items
