class Parent1:
    def __init__(self):
        print("In Parent1 constructor")
    
class Parent2:
    def __init__(self):
        self.x=10
        print("In Parent2 constructor")
    
class Child(Parent1,Parent2):
    pass

Child()   #===> In Parent1 constructor