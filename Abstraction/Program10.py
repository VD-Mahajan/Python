from abc import ABC,abstractmethod


class Parent(ABC):
    @abstractmethod
    def fun(self):
        print('In Parent fun')


class Child(Parent):
    def fun(self):
        print('In Child fun')
        super().fun()


obj = Child()
obj.fun()

'''
Discussion: Unlike Java’s abstract methods or C++’s pure abstract methods, abstract methods as defined here may have an implementation. This implementation can be called via the super mechanism from the class that overrides it. This could be useful as an end-point for a super-call in framework using cooperative multiple-inheritance
'''