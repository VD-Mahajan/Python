from abc import ABC,abstractmethod


class Demo(ABC):

    @abstractmethod
    def __init__(self):
        print('in constructor')


class Memo(Demo):
    def __init__(self):
        print('in memo constructor')


Memo()          #====> in memo constructor