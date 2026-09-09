# num = int(input("Enter the Number : "))

# if num > 0:
#     print("positive number")
# elif num <0:
#     print("Negative number")
# else:
#     print("zero")

# -------------------------------------------
# num2 = int(input("Enter the Number : "))

# if num2 % 2 == 0:
#     print("Even number")
# else:
#     print("Odd Number")



# -------------------------------------------
# also used the max() function
# a = int(input("Enter 1st number : "))
# b = int(input("Enter 2nd Number : "))
# c = int(input("Enter 3rd Number : "))

# if(a > b and a > c):
#     print(a, "is largest number")
# elif(b > a and b > c):
#     print(b , "is lagest number")
# else:
#     print(c, "is largest number")



# -------------------------------------------
# num3 = int(input("Enter number : "))
# for i in range(1, 11):
#     print(num3 , " * ", i , " = " , num3 * i)


# -------------------------------------------
# num = int(input("Enter Number : "))
# sum = 0
# for i in range(1 ,num+1):
#     sum = sum + i
# print(sum)


# -------------------------------------------
# num = int(input("Enter Number : "))
# rev = 0
# while num > 0 :
#     rem = num % 10 
#     rev = rev * 10 + rem 
#     num = num // 10

# print("reverse is : ", rev)



# -------------------------------------------
# num = int(input("Enter Number "))
# sum = 0

# while num > 0:
#    num = num // 10
#    sum = sum + 1

# print("count of digit is  : ", sum)

# -------------------------------------------
# num = int(input("Enter Number : "))
# f = 1

# for i in range(1 , num+1):
#     f = f * i
# print("Factorial : ", f)

# -------------------------------------------
# num = 20
# print("even") if num % 2 == 0 else print("Odd")

# -------------------------------------------

# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 ==0:
#         print("fizzBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)
