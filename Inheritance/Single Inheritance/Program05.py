class Parent:
    def __init__(self):
        print('hi')


class Demo(Parent):

    def __init__(self):
        super().__init__()          #====> hi
        print(super())              #====> <super: <class 'Demo'>, <Demo object>>


Demo()