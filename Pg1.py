a = [11,22,33,44]
b = [1,2,3]
def length(a):
    leng=0
    for x in a:
        leng +=1
    return leng

def add(a,b):
    c = [0]*(length(a) + length(b))
    for i in range(length(c)):
        c[i] = a[i] if i< length(a) else b[i-length(a)]
    return c

c = add(a,b)
print(c)


