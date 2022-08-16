#right shift
a = [11,22,33,44,55,66]
def length(a):
    leng=0
    for x in a:
        leng +=1
    return leng
n=length(a)
r = 3
for j in range(r):
    temp = a[n-1]
    n = length(a)
    for i in range(n-1,0,-1):
        a[i] = a[i-1]
    a[0] = temp

    print(a)


'''

55	11	22	33	44		n=5	
0	1	2	3	4			
							
temp =		a[n-1]		55			
i	a[i]	a[i-1]					
4	a[4]	a[3]		11 22 33 44 44			
3	a[3]	a[2]		11 22 33 33 44			
2	a[2]	a[1]		11 22 22 33 44			
1	a[1]	a[0]		11 11 22 33 44			
a[0]===> 55							
'''
