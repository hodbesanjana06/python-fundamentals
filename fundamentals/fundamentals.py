# Print Function Practice
'''
print("---------------------------------------")
print("Name :", "Sanajna Yashwant Hodbe")
print("Age : ", 23)
print("City : ","Pune"," & ", "Country : ", "India")
print("Welcome to python " )
print("Lerning Fundamentals")
print("sanjana", 20 , 3.1, True)
print("2026", "22", "05", sep="-")
print("hello", end=" ")
print("world..")

'''

# Variable Practice
'''
print("-----------------------------------------")
name = "sanjana"
age = 21
height = 5.25
color = 'blue'
print(" | Name : ", name, " | Age : ", age, " | Height : ", height, " | Color : ", color)

x = 30 
y = 20
print("Addition : ",x + y)
# c = x
# x = y
# y = c
# print("After Swap : ", x , y)
print("Before swaping : ", "X : ", x , "Y : ", y)
y = x+y
x =  y-x
y = y - x

print("After swaping :","X :",x ,"Y :", y)

a = b = c = 10
print("same value to three variables in one line ")
print("A = ",a)
print("B = ",c)

print("multiple variables in one line")
a,b,c = 10, 20, 30
print("A = ", a)
print("B = ", b)
print("C = ", c)

'''

# id() Function Practice
'''
print("----------------------------------------------")
x = 10
y = 10
print("Two variables with the same integer value")
print("X : ",id(x))
print("Y : ",id(y))

print("two different lists and print their id()")
l = [10, 20 ,30]
l2 = [9, 32, 12]
print("l1 = ", id(l))
print("l2 = ", id(l2))


print("Assign one list to another variable and compare")
l=[10, 2, 12]
temp =l

if id(l) == id(temp):
    print("Both are same ")
else:
    print("something will be wrong")

print("Original = ", id(l))
print("Temporary = ", id(temp))

print("two string variables with the same value and compare")
s1 = "sanju"
s2 = "sanju"

if id(s1) == id(s2):
    print("same id")
else:
    print("Not same id")
print("s1",id(s1))
print("s2 ",id(s2))
'''

# Data Types 
'''
print("---------------------------------------")
i = 20
f = 12.1
s = "python"
b = True

print("i = ",i," ",type(i))
print("f = ",f, " ",type(f))
print("s = ",s, " ",type(s))
print("b = ",b, " ",type(b))

fruite = ['apple', 'mango', 'banana', 'orange', 'peru']
print(fruite)

print("---------------tuple------------")
t = (10 , 20 , 30)
print(t)

print("---------------Dictionary---------")
d = {
    'name':'sanjana', 'age':20
}
print(d)


print("----------------Set------------")
s = {1,2,3,1 ,3, 6,4,2,1 ,8}
print(s)

a = 10
b = 2.2
c = "20"
print("int → float ",float(a))
print("float → int ", int(b))
t = float(c)
p = int(t)
print("string → int",p,type(p))

'''

# Input Function Practice

print("-------------------------------------------------------")

name = input("Enter your name ")
print("Welcome ", name)
print("_______________________________")

n1 = int(input("Enter 1st number : "))
n2 = int(input("Enter 2nd number : "))
print("Sum : ", n1 + n2)
print("_______________________________")

age = int(input("Enter Age : "))
print("You are ",age,"years old")
print("_______________________________")


city = input("Enter city : ")
country = input("Enter Country : ")
print("city & country = ",city, country )
print("_______________________________")


n = int(input("Enter Number for square : "))
print("number of square : ", n*n)
print("_______________________________")


l = int(input("enter len "))
w = int(input("Enter width : "))
print("Area : ", l * w)
print("_______________________________")


l = input("Your favorite programming language")
print(l)
print("_______________________________")


n1 = int(input("Enter 1st number : "))
n2 = int(input("Enter 2nd number : "))
n3 = int(input("Enter 3rd number : "))
print("Largest : ", max(n1, n2 , n3))
print("_______________________________")


s = input("Enter one sentence : ")
print(s.upper())
