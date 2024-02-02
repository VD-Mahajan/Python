def func(*args):
    print("start func")
    sum=0
    for i in args:
        sum+=i
        yield sum
    print("end func")

val = func(1,2,3,4,5)

print(next(val))
print(next(val))
print(next(val))
print(next(val))
print(next(val))
# print(next(val))        Error : StopIteration