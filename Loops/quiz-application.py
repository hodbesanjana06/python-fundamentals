c = 0

print("                  Quiz Time                     ",end="\n")
print("------------------------------------------------")
print("1. Python is language or framework?")
a1 = input("").lower()

print("2. int is data type or keyword or both?")
a2 = input("").lower()

print("3. Which is the arithmetic operator? ( & , | , ! , // )")
a3 = input("")

print("4 . Solve the equation 2(1*10)//5")
a4 = input("")

if a1 == "language":
    c += 1

if a2 == "both":
    c += 1

if a3 == '//':
    c += 1

if a4 == '4':
    c += 1


print("_________________________________________________")

print("Your Score:", c)
print("___________")

if c == 2:
    print("upps....give your anothe best & try again")
else:
    print("Congrats....Well Done !")

print("_________________________________________________")
