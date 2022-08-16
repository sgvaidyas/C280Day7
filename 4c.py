a = []
cont = True
while cont:
    a = a + [0]
    ele = int(input("give an ele: "))
    location = 0
    biggest = True
    for j in range(0, len(a)):
        if a[j] >= ele:
            location = j
            biggest = False
            break
    if biggest:
        a[len(a) - 1] = ele
    else:
        key = a[location]
        for m in range(len(a) - 1, location - 1, -1):
            a[m] = a[m - 1]
        a[location] = ele

    print(a)
