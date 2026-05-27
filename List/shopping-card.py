
Items = []


while True:
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Card")
    print("4. Serch Item")
    print("5. Exit")
    
    print("________________________________")
    c = int(input("Enter Your Choice : "))
    print("________________________________")

    if c == 1:
        name= input("Enter the Item name ")
        Items.append(name)
        print("________________________________")

    elif c == 2:
        r = input("Enter remove name : ")
        if r in Items:
            Items.remove(r)
            print("Item Remove")
        else:
            print("Item Not Found")
        
        print("________________________________")


    elif c == 3:
        print("     Card Items      ")
        print(Items)

        print("________________________________")

    elif c == 4:
        s = input("Enter the item for searching : ")
        if s in  Items:
            print(s, "is present in items")
        else:
            print("Not present in items")
        
        print("________________________________")


    elif c == 5:
        print("Exiting program ....")


    else:
        print("Invalid choice ! try again...")

