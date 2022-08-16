a = [11,22,33,44,55,66]

r = 7

print(a[r%len(a):] + a[:r%len(a)] )
