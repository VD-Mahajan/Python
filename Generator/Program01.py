def func(*args):
    sum=0
    for i in args:
        sum+=i
        yield sum
    
def s(a,b):
    while a<b:
        yield a
        a=a+1

for i in s(1,5):
    print(i)

print("="*8)

for i in func(1,5):
    print(i)