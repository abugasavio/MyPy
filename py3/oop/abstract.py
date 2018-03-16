from abc import ABCMeta, abstractmethod


class GetterSetter(metaclass=ABCMeta):

    @abstractmethod
    def set_val(self, input):
        """Set a value on the instance"""
        pass

    @abstractmethod
    def get_val(self):
        """Get and return a value from the instance"""
        pass
