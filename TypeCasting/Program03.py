a=[1,2,3]
b=a
c=[1,2,3]

print(id(a)==id(b))     #True
print(id(a)==id(c))     #False
