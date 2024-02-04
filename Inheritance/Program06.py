class Parent1:
    def __init__(self):
        print("In Parent1 constructor")
    
class Parent2:
    def __init__(self):
        self.x=10
        print("In Parent2 constructor")
    def disp(self):
        print("In Parent2 disp")
        
class Child(Parent1,Parent2):
    pass

Child()
Child().disp()


'''
o/p:
In Parent1 constructor
In Parent1 constructor
In Parent2 disp
'''