class D:
    pass

class E(D):
    pass

class A:
    pass

class B(A):
    pass

class C(A):
    def show(self):
        print("In F")

class F(E,B):
    pass

F().show()

print(F.__mro__)
