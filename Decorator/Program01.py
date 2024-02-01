def outer():
    print("Outer function")
    def inner():
        print("Inner")
    return inner()

outer()