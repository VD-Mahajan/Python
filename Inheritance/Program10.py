class Parent0:
    pass
    def fun(self):
        print('Parent0')
        
class Parent1(Parent0):
    pass
    # def fun(self):
    #     print('Parent1')
    
class Parent2():
    pass
    def fun(self):
        print('Parent2')
    
class Parent3(Parent1,Parent2):
    pass
    # def fun(self):
    #     print('Parent3')
    
class Child(Parent3):
    pass
    # def fun(self):
    #     print('Child')
    
    
c=Child()
c.fun()                         #Parent0
print(Child.mro())              #[<class '__main__.Child'>, <class '__main__.Parent3'>, <class '__main__.Parent1'>, <class '__main__.Parent0'>, <class '__main__.Parent2'>, <class 'object'>]