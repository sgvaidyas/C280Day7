n = int(input("Enter the val of n = "))
a = []
for i in range(n):
    ele = int(input("Enter the ele = "))
    a.append(ele)

shift = int(input("Enter shift val = "))

shift = shift % n
start_ind = -(n - shift)

c = [0]*n
j = 0

for i in range(start_ind, start_ind + n):
    c[j] = a[i]
    j += 1


print(c)

'''
a = [11,22,33,44]

r=6

shift = 6%4 = 2
stind = -(4-2) = -2

j=0
j   i  c[j] j+=1
-----------------------
0  -2   33
1  -1   44
2   0   11
3   22  22

'''
