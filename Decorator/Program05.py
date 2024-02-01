def whoiam(func):
    def inner():
        func()
        print("I am student")
    return inner

@whoiam
def show():
    print("My name is Vishal")
    
show()