def fun():
    print("Start fun")
    yield 10
    print("End fun")


a=fun()
print(next(a))              #===> Start fun
                            #===> 10


'''
a=fun()
print(next(a))
print(next(a))

This generate error : StopIteration
'''


'''
print(next(fun()))
print(next(fun()))

o/p:
Start fun
10
Start fun
10
'''