a = "apple"

print(a.center(60))
print(a.ljust(60))
print(a.rjust(60))


print(a.center(60,'*'))
print(a.ljust(60,'*'))
print(a.rjust(60,'*'))

print(a.upper())
b="hi JamES"
print(b.lower())
print(b.swapcase())


a = " hi this is a sample"
print(a.startswith("hi"))
print(a.startswith(" hi"))
print(a.endswith("le"))
print(a.endswith(" hi"))


b = a.split()
print(b)
a = "hey this, is just a sample, its time !"
b = a.split(',')

print(b)


rec = "111 | Shilpa | 34 | 70000"
print(rec.split('|'))


a = "          jfjkfkj jkljfkljfkle         "
print(a.strip())
print(a.lstrip())
print(a.rstrip())

a = "687676545"
print(a.isdigit())
a="jkjhkjhfkjhj"
print(a.isalpha())

a="jhjg979878"
print(a.isalnum())

a = "A"
print(ord(a))

x = 88
print(chr(x))

a = "hi this is getting boring, boring and boring"
print(a.find("boring"))
print(a.find("boring",22))
print(a.find("boring",22,30))

b = a.replace("boring","very boring")
print(b)


print(b.count("is"))


a = "Ram\n Shyam \n Dhyan\n"
print(a.splitlines())





