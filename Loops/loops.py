#___________________________ FOR LOOP _____________________________________

#     print 1 to 10        
'''for i in range(1 , 11):
    print(i, end=" ")
'''

#       print even number from 1 to 10      
'''for i in range(1, 11):
    if i % 2 == 0:
        print(i ,end=" ")
'''


#       Multiplication of table    
'''     
n = int(input("Enter Number : "))

for i in range(1, 11):
    print(i * n , end=" ")
    
'''

#       Pattern 1 

# # # #         
# # # #         
# # # #         
# # # #          
'''
n = int(input("Enter number : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print("#", end=" ")
    print(end="\n")
'''


#       Pattern 2       

# 
# # 
# # # 
# # # # 

'''
n = int(input("Enter number : "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print("#", end=" ")

    print(end="\n")
    
'''


'''print("     1 to 10 reverse         ")

for i in range(10, 0 , -1):
    print(i, end=" ")

'''

#___________________________ WHILE LOOP _____________________________________
#        count the number 
'''n = int(input("Enter Number : "))
c = 0

if n == 0:
    c = 1
else:
    while n != 0:
        n = n // 10
        c = c + 1

print("Count : ", c)


'''
#       factorial of number         
'''
n = int(input("Enter Number : "))

f = 1
i = 1

while i <= n:
    f = f * i
    i = i + 1

print("factorial is : " , f)

'''

#       SUm of digit
'''n = int(input("Enter  number : "))

t = 0

while n != 0:
    d = n % 10
    t = t + d
    n = n // 10

print("Sum of digit : ", t)

'''

#       Palindrom
'''
n = int(input("Enter the number : "))
temp = n
r = 0

while n != 0:
    d = n % 10
    r = r * 10 + d
    n = n // 10


if temp == r:
    print("Palindrom number ", temp)
else:
    print("Not palindrom num", temp)
    
'''

