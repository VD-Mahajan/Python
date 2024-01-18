#type casting
#float to int
a=1.89
print(int(a))


#bool to int
a=False
print(int(a))

#string to int
a="32"
print(int(a))

#complex to int
a=3+4j
print(type(a))
#print(int(a))      invalid

#int to float
a=2
print(float(a))

#bool to float
a=False
print(float(a))    

print(complex(True))           #=====>(1+0j)
print(complex(False))          #=====> 0j 
print(bool(""))                #=====> False
print(bool("f"))               #=====> True