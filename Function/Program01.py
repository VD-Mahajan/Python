def outer():
    print("In outer")
    def inner():
        print("In Inner")
    return inner
f=outer()
f()