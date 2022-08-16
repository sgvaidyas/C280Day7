a= [1,4,11]
def find(key):
    isFound = False
    for i in range(len(a)):
        if a[i] <= key and a[i+1]>key:
            isFound = True
            return i
    if isFound == False:
        return False
def insert():
    temp = find(ele)
    a.append(0)
    for i in range(len(a)-1,temp+1, -1):
        a[i] = a[i-1]
    a[temp+1] = ele
while True:
    print(a)
    ele = int(input('enter your number'))
    if ele>a[len(a)-1]:
        a.append(ele)
    elif ele<a[0]:
        temp = 0
        a.append(0)
        for i in range(len(a)-1,temp, -1):
            a[i] = a[i-1]
        a[temp] = ele
    else:
        insert()
