def fibo(num):
    a=0
    b=1
    c=a+b
    for i in range(num):
        yield a
        a=b
        b=c
        c=a+b                
     
for i in fibo(10):
    print(i)
       
    