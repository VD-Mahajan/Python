def fun(a,b):
    while(a<b):
        yield a
        a=a+1
    print('End fun')

for i in fun(1,10):
    print(i)