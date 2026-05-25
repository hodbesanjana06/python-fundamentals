
ask = input("Enter Pattern (traiangle / square / pyramid) : ").lower()
n = int(input("Enter the size : "))

if ask == 'traiangle':
    for i in range(1 , n+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print(end="\n")
elif ask == 'square':
    for i in range(1 , n+1):
        for j in range(1 , n+1):
            print("*", end=" ")
        print(end="\n")
elif ask == 'pyramid':
    for i in range(1 , n+1):
        for j in range(n -i):
            print(" ", end=" ")
        for j in range(1 , i +1):
            print(" * ", end=" ")

        print(end="\n")

else:
    print("something is wrong .....enter proper choice !")