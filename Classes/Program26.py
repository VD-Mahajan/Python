class Test:
    @classmethod
    def m1(self):
        print('In m1()')
        print('id of self or cls :{}'.format(id(self)))         #This is class id

t = Test()
t.m1()

print('id of object t :{}'.format(id(t)))           #This is id of object
print('id of object t :{}'.format(id(Test)))        #This is class id