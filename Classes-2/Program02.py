class Parent:
    def disp(self,x):
        print('In Parent disp')
        
class Child:
    def disp(self):
        print('In Child disp')

obj = Child()
obj.disp(10)

'''
    obj.disp(10)
TypeError: disp() takes 1 positional argument but 2 were given
'''
