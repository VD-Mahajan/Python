class A:
    def disp(self):
        print('A')

class B:
    def disp(self):
        print('B')
        
class C(A,B):
    pass

C().disp()     #===> A