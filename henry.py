aList = [3,5,7]
while True:
    choice = int(input(("1 INSERT, 2 DISPLAY, 3 EXIT  --> ")))
    if choice == 1:

        ele = int(input("Which number would you like to input?"))
        choice = int(input(("1 INSERT BEFORE, 2 INSERT AFTER ")))
        while choice not in [1,2]:
            choice = int(input(("1 INSERT BEFORE, 2 INSERT AFTER ")))
        msg = "before" if choice ==1 else "after"
        pos = int(input(f"Which element would you like to insert {ele} {msg}?"))
        if pos not in aList:

            aList.append(ele)
            print(f"{pos} is not in list. {ele} has been appended to List.")
            continue
        else:
            print("Adding",ele)
            for i in range(length(aList)):
                if aList[i] == pos and choice == 1:
                    temp = aList[length(aList)-1]
                    aList.append(0)
                    for i in range(length(aList) - 1, i-1, -1):
                        aList[i] = aList[i - 1]
                    aList[i] = ele
                    print("List is now",aList)
                    break
                elif aList[i] == pos and choice == 2:

                    temp = aList[i]
                    aList.append(0)
                    for i in range(length(aList) - 1, i - 1, -1):
                        aList[i] = aList[i - 1]
                    aList[i] = temp
                    aList[i + 1] = ele
                    print("List is now", aList)
                    break
    elif choice == 2:
        print(aList)
    elif choice ==3:
        break
