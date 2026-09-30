


# def positive(num):
#     if num >0:
#         print("Positive number ")
#     elif num == 0:
#         print("Zero")
#     else:
#         print("Negative")
# -----------------------------------------------
# def Even_odd(num):
#     if num % 2 == 0:
#         print("Even number : ") 
#     else:
#         print("Odd number ")
# -----------------------------------------------

# def sum_digit(num):
#         total = 0
#         while num > 0:
#              r = num % 10
#              total = total + r
#              num = num // 10
#         return total
# -----------------------------------------------

# def rev(num):
#      answer = 0

#      while num > 0:
#         rem = num % 10
#         answer = answer * 10 + rem
#         num = num // 10
#      return  answer
# ----------------------------------------------

# def prime(num):
#     f = 1

#     if num <= 1:
#         f = 0
#     else:
#         for i in range(2 , num):
#             if num % i == 0:
#                 f = 0
#                 break

#     if f == 1:
#         print("prime number")
#     else:
#         print("Not prime number ")

#     print()     
# -----------------------------------------------


# num = int(input("Enter Number : "))
# positive(num)
# print("Sum : ",sum_digit(num))
# print("rev : ",rev(num))
# Even_odd(num)
# prime(num)