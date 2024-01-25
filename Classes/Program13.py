def Test():
    print("In function")
    
class Test:
    def __init__(self):
        print("In constructor")
    def Test(self):
        print("In class function")  

Test()   #====> In constructor   (constructor overwrite the method)