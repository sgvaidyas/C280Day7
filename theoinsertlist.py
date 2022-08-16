def task4(listA, data, element, before):
    newList = []
    added = 0
    if data not in listA:
        newList = listA + [element]

    else:
        for i in listA:
            if i == data and added != 1:
                if before == 1:
                    newList += [element]
                    newList += [i]
                    added = 1
                else:
                    newList += [i]
                    newList += [element]
                    added = 1
            else:
                newList += [i]
    return newList


if __name__ == '__main__':
    listA = [11, 22, 33, 44, 55, 66]
    while True:
        elem = int(input("Insert a number: "))
        data = int(input("Before or After which number: "))
        before = int(input("Would you like it: \n1.Before \n2. After\n"))
        listB = task4(listA, data, elem, before)
        print(listB)
        listA = listB
        if int(input("Press: \n1.Continue \n2. Exit\n")) == 2:
            break
