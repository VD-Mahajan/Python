from abc import ABC, abstractmethod


class Demo(ABC):
    @abstractmethod
    def fun(self):
        print('in abstract fun')


class Memo(Demo):         #==> Class Memo must implement all abstract methods
    pass

Memo()

'''
error reason :
TypeError: Can't instantiate abstract class Memo without an implementation for abstract method 'fun'

'''