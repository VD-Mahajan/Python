def whoiam(func):
    print("I am student")
    return func

@whoiam
def show():
    print("My name is Vishal")
    
show()
