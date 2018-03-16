from abc import ABCMeta, abstractmethod


class GetSetParent(metaclass=ABCMeta):
    def set_val(self, value):
        self.val = value

    def get_val(self):
        return self.val

    @abstractmethod
    def show_doc(self):
        pass


class GetSetInt(GetSetParent):
    def set_val(self, value):
        if not isinstance(value, int):
            value = 0
        super(GetSetInt, self).set_val(value)

    def show_doc(self):
        print('GetSetInt Object ({}), only accepts integer values'.format(self))
