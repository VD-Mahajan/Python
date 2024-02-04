def fun():
    print("Start fun")
    yield 1
    yield 2
    yield 3
    print("running fun")
    yield
    
a=fun()
print(next(a))
print(next(a))
print(next(a))

if(next(a))==None:
    pass