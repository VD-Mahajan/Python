from abc import ABC, abstractmethod


class Parent(ABC):

    def __init__(self):
        self.a = 10
        print('In Parent constructor')
        print(id(self))

    @abstractmethod
    def marry(self):
        print(id(self))
        print('hello world')


class Child(Parent):

    def __init__(self):
        super().__init__()
        print('In Child constructor')

    def marry(self):
        print(id(self))
        Child().marry()
        # print(self.a)
        print('hi')


obj = Child()
obj.marry()
# print(id(obj))



# In Parent constructor
# 1425033452608
# In Child constructor
# 1425033452608
# In Parent constructor
# 1425033452656
# In Child constructor
# 1425033452656
# Traceback (most recent call last):
#   File "D:\Python Pycharm\Python\Abstraction\Program11.py", line 31, in <module>
#     obj.marry()
#   File "D:\Python Pycharm\Python\Abstraction\Program11.py", line 25, in marry
#     Child().marry()
#   File "D:\Python Pycharm\Python\Abstraction\Program11.py", line 25, in marry
#     Child().marry()
#   File "D:\Python Pycharm\Python\Abstraction\Program11.py", line 25, in marry
#     Child().marry()
#   [Previous line repeated 995 more times]
#   File "D:\Python Pycharm\Python\Abstraction\Program11.py", line 20, in __init__
#     super().__init__()
# RecursionError: maximum recursion depth exceeded
