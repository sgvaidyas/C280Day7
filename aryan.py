a = []
cont = True
while cont:
    option = int(input("Choose an option 1,2,3"))
    if(option ==1):
        a = a + [0]
        ele = int(input("give an ele"))
        after = int(input("give an element to insert after"))
        location = 0
        isFound = False
        for j in range(0,len(a)):
            if (a[j] == after):
                isFound = True
                location = j
                break
        if(isFound == False):
            a[len(a)-1] = ele
        else:
            for m in range(len(a)-1,location,-1):
                a[m] = a[m-1]
            a[location+1] = ele
        print(a)
    elif(option == 2):
        print(a)

    elif(option == 3):
        cont == False
    else:
        print("please select an option: 1,2,3")
    #key = a[index]
