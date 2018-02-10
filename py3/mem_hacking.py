class MutableThing:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


mutable_things = MutableThing(1, 2, 3, 4)
print(mutable_things.__dict__)


class ImmutableThing:
    __slots__ = ['a', 'b', 'c', 'd']

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


immutable_thing = ImmutableThing(1, 2, 3, 4)
