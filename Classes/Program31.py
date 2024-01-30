class Test:
    a = 10
    def m1(self):
        self.a = 888           # this value is changed for particular instance of the class

t1 = Test()
t1.m1()
print(Test.a)
print(t1.a)