#left shift

a = [11,22,33,44,55,66]
def length(a):
    leng=0
    for x in a:
        leng +=1
    return leng

r = 3
for j in range(r):
    temp = a[0]
    n = length(a)
    for i in range(n-1):
        a[i] = a[i+1]
    a[n-1] = temp

    print(a)


'''

22	33	44	55	11		n=5							
0	1	2	3	4									
													
temp =		a[0]	11										
	i	a[i]	a[i+1]										
	0	a[0]	a[1]		22 22 33 44 55					for i in range(n-1):			
	1	a[1]	a[2]		22 33 33 44 55						a[i]=a[i+1]		
	2	a[2]	a[3]		22 33 44 44 55								
	3	a[3]	a[4]		22 33 44 55 55								
a[n-1] = temp													


'''
