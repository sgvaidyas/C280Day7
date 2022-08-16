def length(a):
    leng=0
    for x in a:
        leng +=1
    return leng


aList = [2,5,7,13,40]
ele = int(input("Input a value --> "))
if not aList:
    aList.append(ele)
for i in range(length(aList)):
    if ele < aList[i] :
        aList.append(0)
        for i in range(length(aList) - 1, i - 1, -1):
            aList[i] = aList[i - 1]
        aList[i] = ele
        break
    if i ==length(aList)-1:
        aList.append(ele)
print(aList)
