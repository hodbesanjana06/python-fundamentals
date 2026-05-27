print("         Email Validator          ")
print("_____________________________________")

mail = input("Enter email : ")

if " " in mail:
    print("remove the space")
elif "@" in mail and "." in mail:
    print("Valid")
else:
    print("Invalid check it contains (@, .)")

print("_____________________________________")