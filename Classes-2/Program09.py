class Parent:
    name = ''

    def myname(self):
        print(f'My name is {self.name}')


def run(self, name):
    print('instance variables are initialized')
    self.name = name


def fun(self, name):
    print('Object is created')
    return object.__new__(self)


Child = type('Child', (Parent,), {'__init__': run, '__new__': fun})

c = Child('Vishal')
c.myname()
print(c)

