class Test:
    
    def __init__(self):
        print('no-arg constructor')

    def __init__(self,x):                       # Overwrite the constructor
        print('one-arg constructor')

t = Test(10)
t = Test()                # Error : __init__() missing 1 required positional argument: 'x'