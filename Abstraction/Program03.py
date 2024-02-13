from abc import ABC,abstractmethod


class Demo(ABC):
    @abstractmethod
    def fun(self):
        print('in abstract fun')


obj = Demo()
obj.fun()


'''
obj = Demo()
          ^^^^^^
TypeError: Can't instantiate abstract class Demo without an implementation for abstract method 'fun'

'''