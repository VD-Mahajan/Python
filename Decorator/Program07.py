def outer1(func):
    print("start outer 1")
    def inner1():
        print("start inner 1")
        func()
        print("end inner 1")
    return inner1

def outer2(func):
    print("start outer 2")
    def inner2():
        print("start inner 2")
        func()
        print("end inner 2")
    return inner2

@outer2
@outer1
def myfunc():
    print("my function")

myfunc()