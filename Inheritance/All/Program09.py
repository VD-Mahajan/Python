class Parent1:
    def fun(self):
        print('Parent1')
    
class Parent2(Parent1):
    pass
    # def fun(self):
    #     print('Parent2')
    
class Parent3(Parent1):
    pass
    # def fun(self):
    #     print('Parent3')
    
class Child(Parent2,Parent3):
    pass
    # def fun(self):
    #     print('Child')
    
    
c=Child()
c.fun()
print(Child.__mro__)  #(<class '__main__.Child'>, <class '__main__.Parent2'>, <class '__main__.Parent3'>, <class '__main__.Parent1'>, <class 'object'>)


'''
first priority: Child
2nd : Parent2
third : Parent3
last : Parent1

'''