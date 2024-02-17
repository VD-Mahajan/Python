from abc import ABC, abstractmethod

class Parent(ABC):

    def __init__(self):
        print('Parent constructor')

    @abstractmethod
    def marry(self):
        print(id(self))
        print('hello world')


class Child(Parent):
    def marry(self):
        print(id(self))
        super().marry()
        print('hi')


obj = Child()
obj.marry()


'''
Parent constructor
1436755057872
1436755057872
hello world
hi
'''