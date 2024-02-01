def decor(fun):
    def inner(name):
        if(name == 'Shashi'):
            print('Teacher')
        else:
            fun(name)
    return inner

@decor
def fun(name):
    print('Student')

fun('Vishal')
fun('Shashi')