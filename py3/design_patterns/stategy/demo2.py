from abc import ABCMeta, abstractmethod

# the interface
class AbsStrategy(metaclass=ABCMeta):
    @abstractmethod
    def calculate(self, order):
        """ Calculate shipping cost"""

# this is the context
class ShippingCost:
    def __init__(self, strategy):
        self._strategy = strategy

    def shipping_cost(self, order):
        self._strategy.calculate(order)

# the various concrete stategis
class FedExStrategy(AbsStrategy):
    def calculate(self, order):
        return 3.00

class PostStrategy(AbsStrategy):
    def calculate(self, order):
        return 5.00
 
class UPSStrategy(AbsStrategy):
    def calculate(self, order):
        return 4.00
