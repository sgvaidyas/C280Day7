lst = [[""] * 3]


def find_index(lst, num):
    ind = 0
    for each in lst:
        if each >= num:
            break
        ind += 1
    if ind > len(lst):
        return False
    return ind


def check_valid(phone, i):
    for x, each in enumerate(lst):
        if each[i] == phone:
            return x
    return False


def my_append():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    while check_valid(phone, 1):
        print("Not unique number!")
        phone = input("INVALID! Enter Valid Phone Number:")
    email = input("Enter Email Address: ")

    if not name or not phone or not email:
        print("No empty data please!")
        return 0

    lst.append([name, phone, email])
    print("ADDED:", *lst[-1])


def print_phone_book():
    print("NAME\tPHONE\tEMAIL")
    for each in lst[1:]:
        for s in each:
            print(s.center(15), end='\t')
        print("")


def print_menu():
    print("Phonebook")
    print("1 Insert")
    print("2 Delete")
    print("3 Search")
    print("4 Update")
    print("5 Display")
    print("6 Exit")


def delete_by_phone():
    phone = str(input("Enter Phone Number to Delete: "))
    x = check_valid(phone, 1)
    if x:
        del lst[x]
    else:
        print("Not found!")


def update_by_phone():
    phone = str(input("Enter Phone Number to Update: "))
    x = check_valid(phone, 1)
    if x:
        name = input("Change name? Leave emtpy for no.")
        if name:
            lst[x][0] = name
        phone = input("Change phone number? Leave emtpy for no.")
        if phone:
            tmp = lst[x][1]
            lst[x][1] = ""
            if check_valid(phone, 1):
                print("Not unique number!")
                lst[x][1] = tmp
                return 0
            lst[x][1] = phone
        email = input("Change email? Leave emtpy for no.")
        if email:
            lst[x][2] = email
        print("ENTRY UPDATED:", lst[x])
    else:
        print("Not found!")


def search_by_phone():
    phone = str(input("Enter Phone Number to Search: "))
    x = check_valid(phone, 1)
    if x:
        print(*lst[x])
    else:
        print("Not found!")


if __name__ == '__main__':
    print_menu()
    while True:
        inp = int(input("Menu Choice: "))
        if inp == 1:
            my_append()
        elif inp == 2:
            delete_by_phone()
        elif inp == 3:
            search_by_phone()
        elif inp == 4:
            update_by_phone()
        elif inp == 5:
            print_phone_book()
        elif inp == 6:
            break
