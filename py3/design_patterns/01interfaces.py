import abc

class MyABC(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def do_something(self):
        pass

    @abc.abstractproperty
    def some_property(self):
        pass


class MyClass(MyABC):
    
    def __init__(self, value=None)
        self._myprop = value

    def do_something(self):
        pass

    def some_property(self):
        pass
