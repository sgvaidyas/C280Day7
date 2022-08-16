def task5(listB, element):
    newList = []
    if len(listB) == 0 or element >= listB[len(listB)-1]:
        newList += listB + [element]
        print(newList)
    else:
        for i in range(0, len(listB)):
            if element <= listB[i]:
                newList += [element]
                newList += [listB[i]]
            else:
                newList += [listB[i]]
    return newList


if __name__ == '__main__':
    listA = []
    while True:
        elem = int(input("Insert a number: "))
        listB = task5(listA, elem)
        print(listB)
        listA = listB
        if int(input("Press: \n1.Continue \n2. Exit\n")) == 2:
            break
