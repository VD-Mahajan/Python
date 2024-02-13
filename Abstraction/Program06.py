from abc import ABC, abstractmethod


class Demo(ABC):
    @abstractmethod
    def fun(self):
        print('in abstract fun')


class Memo(Demo):
    def fun(self):
        print('in abstract fun')

Demo()

'''
It doesn't matter you provide implementation for abstract method of Demo or not 
code will run
if you try to instantiate Demo() then only it will give error irrespective of anything
'''