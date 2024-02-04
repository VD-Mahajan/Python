class Parent1:
    pass

class Child(Parent1,Parent1):
    pass

Child()     #TypeError: duplicate base class Parent1