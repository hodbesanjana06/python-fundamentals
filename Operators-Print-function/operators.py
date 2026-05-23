# Print Function Practice Questions
'''
print("----------------------------------------")

print("python" * 5)
print("___________________________________")

print("sanjana",end=" ")
print("hodbe")
print("___________________________________")

print(10,20,30, sep='-')
print("apple",'banana','mango', sep='*')
print("sanjana","hodbe", sep='_')
print(1, 2, 3,4,5 , sep='@')
print(2026, 5, 23, sep='.')
print("python",'java','C++', sep='-')
print("A","B","c","D", sep=':')

'''

# Operators
'''
print("----------------------------------------")
print("         Arithematic operators          ")
a = 10
b = 2
c = 15
print("Add = ", a + b)
print("Sub = ", a - b)
print("Multiply = ", a * b)
print("Divide = ", a / b)
print("Reminder = ", a % b)
print("Power = ", a ** b)
print("Floor division = ", a // b)
print("Average = ", (a+b+c)/3)
l = int(input("Enter len : "))
w = int(input("Enter width : "))
print("Area of Rectangle : ", l * w)

'''


'''
print("----------------------------------------")
print("         Comparison operators           ")

a , b = 10 , 5
print("A = ", a, " | ", "B = ", b)
print("A > B = ", a > b)
print("Equal = ", a == b)
print("5 <= 10 : ", 5 <= 10)

'''

'''
print("----------------------------------------")
print("         Logical operators              ")

print("result of True and False : ",True and False)
print("result of True or False : ",True or False)
print("result of not True  : ",not True )
print('15 > 10 and 15 < 20 : ',15 > 10 and 15 < 20)
print('10 // 2 and 10 // 5 : ', 10 // 2 and 10 // 5)

'''

'''
print("----------------------------------------")
print("         Assignment operators           ")

a=b=c=d=e = 10
print("Value of A , B , C , D, E = ", a)
a += 1
b -= 1
c *= 1
d /= 1
e %= 1

print("+=1 ",a)
print("-=1 ",b)
print("*=1 ",c)
print("/=1 ",d)
print("%=1 ",e)


'''

print("----------------------------------------")
print("         Mixed Practice                 ")

a = 2
print("Square of numver : ", a **2)
print("Cube of number : ", a ** 3)
print("___________________________________")

p = int(input("Enter principle amt : "))
r = int(input("Enter rate of intrest : "))
n = int(input("Enter number of years : "))

s = p * r/100 * n 

print("Simple Interest : ", s)
print("___________________________________")

print("0 and 5 : ", 0 and 5)
print("1 or 0 : ", 1 or 0)
print("not(5  > 2) : ",not(5  > 2))