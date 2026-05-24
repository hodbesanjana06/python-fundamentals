# Control Flow STatement 
'''
print("         Even or Odd         ")
n = int(input("Enter Number : "))
if n % 2 == 0:
    print(n, " is Even number ")
else:
    print(n, " is Not Even number ")
    
'''

'''
print("        Positive , Negative or Zero      ")
n = int(input("Enter Number : "))

if n > 0:
    print("Positive Number")
elif n == 0:
    print("Zero Number ")

else:
    print("Negative Number ")
    
'''

'''

print("         Largest of 2 Numbers        ")
n1 = int(input("Enter 1st Number : "))
n2 = int(input("Enter 2nd Number : "))

if n1 > n2 :
    print(n1, "greater number ")
else:
    print(n2, "greater number ")

print("Largest : ", max(n1, n2))

'''

'''

print("         Largest of 3 Numbers        ")
n1 = int(input("Enter 1st Number : "))
n2 = int(input("Enter 2nd Number : "))
n3 = int(input("Enter 3rd Number : "))

if n1 > n2 and n1 > n3:
    print(n1," is greater ")
elif n2 > n1 and n2 > n3:
    print(n2,"is greater ")
else:
    print(n3,"is greater ")

print("MAX : ", max(n1, n2, n3))
print("min : ", min(n1, n2,n3))

'''

'''
print("     Divisible by 5 & 11     ")
n = int(input("Enter Number : "))

if n % 5 == 0 and n % 11 == 0:
    print("Number is divisible by 5 and 11")
else:
    print("Number is Not divisible by 5 and 11")
'''


'''
print("     Vowel or Consonant      ")
c = input("Enter character : ")

if c in "aeiouAEIOU":
    print(c," is the vowel")
else:
    print(c , "is conconent")
    
'''

'''

print("         Alphabet or Not         ")
s = input("Enter character ")
if s.isalpha():
    print("alphabet")
else:
    print("not alphabet ")

'''


'''
c = input("Enter character : ")
if c.isupper():
    print(c, "character is upeer ")
else:
    print(c, "Character is lower")
    
'''


'''
print("        Character Type Checker         ")

c = input("Enter character : ")

if c.isalpha():
    print(c, "is the alphabet")
elif c.isnumeric():
    print(c, "is Digit")
else:
    print(c, "is special character")
    
'''

'''
print("     Absolute Value          ")
n = int(input("Enter Negative number : "))

print("Positive number : ", (n * -1))

'''

'''

print("         Profit or Loss          ")

c = int(input("Enter Cost Price :"))
s = int(input("Enter Selling Price : "))

if c > s:
    print("Loss")
elif c == s :
    print("No profit , no loss")
else:
    print("Profit")
    
'''

'''
print("     Triangle Validity       ", end="\n")
a1 = int(input("Enter Angle 1 : "))
a2 = int(input("Enter Angle 2 : "))
a3 = int(input("Enter Angle 3 : "))

if a1 + a2 + a3 == 180 :
    print("make the triangle ")
else:
    print("not make the triangle ")

'''


'''
print("         Triangle Type           ")

s1 = int(input("Enter side 1 : "))
s2 = int(input("Enter side 2 : "))
s3 = int(input("Enter side 3 : "))

if s1 == s2 == s3:
    print("Equilateral Triangle")
elif s1 == s2 or s2 == s3 or s1 == s3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

'''


'''

print("         Calculator Using Conditions          ")

n1 = int(input("Enter 1st number : "))
n2 = int(input("Enter 2nd number : "))

o = input("Enter Operator (+ , - , * , /, %) : ")

if o == "+":
    print("Addition : ", n1 + n2)
elif o == "-":
    print("Substraction : ", n1 - n2)
elif o == "*":
    print("Multiplication : ", n1 * n2)
elif o == "/":
    print("Division : ", n1 / n2)
elif o == "%":
    print("Modulation : ", n1 % n2)
else:
    print("Invalid")
    
'''


'''print("     Admission Eligibility           ")

m = int(input("Enter math marks : "))
p = int(input("Enter physics marks : "))
c = int(input("Enter chemistry marks : "))

if m > 65 and p > 55 and c > 50:
    print("you are eligible ")
else :
    print("Not eligible ")

'''

'''
print("         Check Coordinate Position           ")

x = int(input("Enter X "))
y = int(input("Enter Y "))

if x == 0 and y == 0:
    print("Origin")
elif y == 0 and x != 0:
    print("On X-axis")
elif x == 0 and y != 0:
    print("On Y-axis")
else:
    print("invalid")

'''
u = "admin"
pas = "pass123"

username = input("Enter Username : ")
p = input("Enter Password : ")

if username == u and p == pas:
    print("Login Sucessfully....")
else:
    print("Something went wrong try again....")

