from abc import ABC,abstractmethod


class Demo(ABC):

    def fun(self):
        print('In fun')             #===> In fun


obj = Demo()
obj.fun()