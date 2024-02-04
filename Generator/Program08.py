def fun():
    print("Start")
    yield 10
    yield 20
    yield 30
    print("End")

a=fun()

print(next(a))
print(next(a))
print(next(a))

try:
    print(next(a))
except:
    pass