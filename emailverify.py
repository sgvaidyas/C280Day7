email = input("Enter the email = ")
invalid = False
#aaaa@jjjj.hhh
l = email.split('@')
print(l)
if len(l)!=2:
    invalid = True
else:
    #l[0] = 'jgjhg'
    #l[1] ='hhh.com'
    #      =['hhh' , 'com']
    t = ('co','com','org','in')
    for x in t:
        temp = l[1].split()
        if len(temp[0])>0  and temp[1]==x:
            print("Valid ")
            break
    else:
        invalid = True

print(invalid)
