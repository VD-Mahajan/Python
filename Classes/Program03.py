class Parent:
    def fun(self):
        print(id(self))
    
class Child(Parent):
    def __init__(self):
        pass
    def fun(self):
        super().fun()
        print(id(self))
        print("Child fun")

obj = Child()
obj.fun()