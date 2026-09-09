# _______________________________________________
#                   String
# _______________________________________________

# name = input("Enter String : ")
# print("Original : ", name)
# print("Reverse : ", name[::-1])


# -------------------------------------------
# name = input("Enter String : ")
# print("Number of characters : ", len(name))



# -------------------------------------------
# name = input("Enter String : ")
# c=0

# for i in name :
#     if "a" in i or "e" in i or "i" in i or "o" in i or "u" in i:
#         c = c + 1  
#         print(i)
# print("Vowel Count : ", c)



# -------------------------------------------
# name = input("Enter String : ")
# rev = name[::-1]
# print(rev)
# if name in rev:
#     print("Palindrom string")
# else:
#     print("not palindrom")

# -------------------------------------------
# name = input("Enter String : ")
# char = input("Enter Character : ")
# c = 0
# for i in name:
#     if char in i:
#         c = c + 1
# print(char , " Occurs ", c ," times")



# -------------------------------------------

# name = input("enter string : ")
# c={}
# for i in name:
#     if i in c :
#         c[i] = c[i] + 1
#     else:
#          c[i]=1
# print(c)
    


# _______________________________________________
#                   List
# _______________________________________________

# lan = ["react", "js" , "py" , "DSA" , "django"]
# print(lan)
# print("First Element : ", lan[0])
# print("Last Element : ", lan[-1])
# print("Total Elements : ", len(lan))

# -------------------------------------------
# skills = ["Python", "React"]
# skills.append("Django")
# print("Append : ",skills)
# skills.insert(0, "Javascript")
# print("Insert : ", skills)
# skills.extend(["HTML", "CSS"])
# print("Extends : ",skills)


# -------------------------------------------
# numbers = [10, 20, 30, 40, 50]
# print(numbers)
# numbers.remove(30)
# print("remove 30 : ",numbers)
# print("Last element : ", numbers.pop())
# print(numbers)


# -------------------------------------------

# numbers = [45, 12, 89, 23, 67]
# print(numbers)
# print("Max : ", max(numbers))
# print("Min : ", min(numbers))


# -------------------------------------------
# numbers = [10, 20, 30, 40, 50]
# print(numbers)
# sum= 0
# for i in numbers:
#     sum = sum + i 
# print("Sum : ",sum)



# -------------------------------------------
# numbers = [10, 15, 22, 33, 40, 51]
# e= 0
# o = 0

# for i in numbers:
#     if i % 2 == 0 :
#         e = e + 1
#     else :
#         o = o + 1
# print("Even count : ", e)
# print("Odd Count : ", o)


# -------------------------------------------
# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# size = len(numbers)
# for i in range(size , 0, -1):
#     print(i)


# -------------------------------------------
# numbers = [10, 20, 5, 40, 30]
# s = numbers.sort()
# print(numbers)
# print("Second Largenst : ", numbers[-2])


# -------------------------------------------
marks = [78, 85, 92, 67, 88]
total = 0
c = 0
for i in marks:
    total = total + i

for i in marks:
    if i >= 80 :
        c = c + 1
print(marks)
print("Total marks : ", total)
print("Highest marks : ", max(marks))
print("Lowest marks : ", min(marks))
print("Number of students who scored above 80 : ", c)
print("Average : ", total // len(marks))

