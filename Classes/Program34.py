class Test:
    x = 30
    
    def __init__(self):
        self.y = 40

    @classmethod
    def fun(cls):
        x = 10
        print(x)
        print(cls.y)       # AttributeError: type object 'Test' has no attribute 'y'

t = Test()
t.fun()