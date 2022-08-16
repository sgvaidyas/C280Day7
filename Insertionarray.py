a = []

def insert(ele,data,ch):
    if data not in a:
        a.append(ele)
    else:
        pos=0
        for i in range(len(a)):
            if a[i] == data:
                a.append(0)
                if ch==2: #after
                    pos+=1
                for j in range(len(a)-1,pos,-1):
                    a[j] = a[j-1]
                a[pos]=ele
                break
            pos+=1

while True:
    ele = int(input("Enter ele  = "))
    data = int(input("Enter the data before/after u would like to insert ele = "))
    ch = int(input("Please insert the choice 1 => before or 2=> after = "))
    insert(ele,data,ch)
    print(a)
