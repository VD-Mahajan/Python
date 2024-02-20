import zope.interface


class MyInterface(zope.interface.Interface):
    x = zope.interface.Attribute('Interface Attribute')

    def m1(self):
        pass

    def m2(self,x):
        pass


print(type(MyInterface))
print(MyInterface.__name__)

x = MyInterface['x']
print(x)
print(type(x))
