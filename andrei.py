a = []
while True:

    print("1: Insert")
    print("2: Display")
    print("3: Exit")
    choice = eval(input("Please make a choice: "))
    if choice == 1:

        val = eval(input("What value do you want to insert? "))
        target = eval(input("Before what value do you want to insert? "))
        ix = -1

        for x in range(len(a)):
            if a[x] == target:
                ix = x

        if ix == -1:
            a.append(val)

        else:
            a.append(0)
            for x in range(len(a)-1, ix, -1):
                a[x], a[x-1] = a[x-1], a[x]
            a[ix] = val
        print(a)
    elif choice == 2:
        print(a)
    elif choice == 3:
        break
