def new(cls):
    print('object is created')
    return object.__new__(cls)


def myfunc(self):
    print('In myfunc')


Demo = type('Demo', (), {'__new__': new})
obj = Demo()

print(obj)




