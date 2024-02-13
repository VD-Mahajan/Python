from abc import ABC,abstractmethod


class Demo(ABC):

    def __init__(self):
        print('in constructor')


Demo()      #====> in constructor