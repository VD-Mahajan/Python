def maxNum(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

def minNum(a,b,c):
    if(a<b and a<c):
        return a
    elif(b<a and b<c):
        return b
    else:
        return c

def answer(a,b,c):
    first=maxNum(a,b,c)
    second=minNum(a,b,c)
    return first+second

print(answer(-3,-5,8))