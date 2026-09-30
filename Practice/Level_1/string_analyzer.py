def rev(text):
    print("Reverse : ",text[::-1])
# -----------------------------------------------

def check(text):
    c=0
    for i in text:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            c = c + 1     
        else:
            pass
    print("Total vowels : ", c)
# -----------------------------------------------

def palindrom(text):
    fake = text[::-1]

    if fake == text:
        print("Palindrom string")
    else:
        print("Not palindrom")
# -----------------------------------------------

def spaces(text):
    new = text.replace(" ", "")
    print(new)
# -----------------------------------------------

text = input("Enter string : ")

rev(text)
check(text)
palindrom(text)
spaces(text)
