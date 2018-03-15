class Queue:
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        item = self._items[0]
        del(self._items[0])
        return item

    def clear(self):
        self._items = []

    def __iter__(self):
        for item in self._items:
            yield item
