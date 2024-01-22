def gun():
    print("In gun")

def run(y):
    print("In run")
    return y            

'''y()   ===> It will give error , because it will call gun function immediately Return the function without calling it'''

def fun(x):
    print("In fun")
    x()

fun(run(gun))
