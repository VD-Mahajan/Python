class Parent:
    x=30
    
class Child(Parent):
    x=10

child = Child()

print(child.x)  
print(Child.x)