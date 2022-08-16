a = [11,22,33,44,55,66]
   # 66 11 22 33 44 55
   # 55 66 11 22 33 44
r = 20%len(a)
right_shift = a[-r:] + a[:-r]
print(right_shift)
