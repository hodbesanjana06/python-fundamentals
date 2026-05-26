
import random


print("         Username Generator          ")
print("_____________________________________")
name = input("Enter first & last Name : ")

s= name.split()
n = random.randint(10,30)
t = s[0][0] + s[1] + str(n)

print(end="\n")
print(t)

print("_____________________________________")
