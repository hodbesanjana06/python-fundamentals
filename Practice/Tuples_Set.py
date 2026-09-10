# _______________________________________________
#                   Tuples
# _______________________________________________

# sub = ("py", "Django" , "React" , "JS")
# print(sub)
# print("First : ", sub[0])
# print("Last : ", sub[-1])
# print("Length : ", len(sub))



# -------------------------------------------
# numbers = (10, 20, 30, 20, 40, 20)
# print("20 Occure : ", numbers.count(20) , "times")
# print("Index of 40 : ", numbers.index(40))


# -------------------------------------------
# person = ("Sanjana", 22, "React")
# name , age , skills = person
# print("name : ", name , " | Age : ", age , " | Skill : ", skills)



# _______________________________________________
#                  Sets
# _______________________________________________
# numbers = [10, 20, 20, 30, 30, 40, 40, 50]
# print("Old" , numbers)
# newset = set(numbers)
# print(newset)



# -------------------------------------------
# skills = {"Python", "React", "Django"}
# print(skills)
# skills.add("Javascript")
# print("Add JS : ",skills)
# skills.remove("React")
# print("remove react : ", skills)



# -------------------------------------------
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
# print(a , b)
# print("Common : ", a & b)
# print("Union : ", a | b)
# print("Diffrence : ", a - b , b -a )
# print("Duplicates : ", )


# -------------------------------------------
# numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]
# print(numbers)
# seen = set()
# duplicate = set()

# for i in numbers:
#     if i in seen:
#         duplicate.add(i)
#     else:
#         seen.add(i)

# print("Duplicates : ",duplicate)



# -------------------------------------------
# developer1 = {"Python", "Django", "React", "Git"}
# developer2 = {"Python", "JavaScript", "React", "HTML"}
# print(developer1 , " || ", developer2)
# print("Skills both developers know : ", developer1 & developer2)
# print("Skills only developer 1 knows : ", developer1 - developer2 )
# print("Skills only developer 2 knows : ", developer2 - developer1 )
# print("All unique skills : ", developer1.union(developer2))





# _______________________________________________
#                  Dictionary
# _______________________________________________
# person ={
#     "name" : "sanjana",
#     "age" : 23,
# }
# print(person)
# person["city"]= "pune"
# person["course"] = "BCA"
# person["age"] = 20

# for key , values in person.items():
#     print(key , " : " , values) 





# -------------------------------------------
# numbers = [1, 2, 2, 3, 1, 4, 2, 3]

# d = {}

# for i in numbers:
#     if i in d:
#         d[i] = d[i] + 1  
#     else :
#         d[i] = 1    #{1 : 1}

# print(d)



# -------------------------------------------
# student = {
#     "name": "Sanjana",
#     "marks": {
#         "Python": 85,
#         "Django": 78,
#         "React": 90
#     }
# }

# print(student)
# print("Name : ", student["name"])
# print("Py marks : ", student["marks"]["Python"])

# for key , values in student.items():
#     if key in "marks":
#         print(values)

# sum =0
# for key , values in student.items():
#     if key == "marks":
#         for subject , mark in values.items():
#             sum = sum + mark

# print(sum)



# -------------------------------------------
# students = [
#     {"name": "Amit", "marks": 75},
#     {"name": "Riya", "marks": 92},
#     {"name": "Rahul", "marks": 68},
#     {"name": "Priya", "marks": 88}
# ]
# sum = 0
# max = students[0]["marks"]
# for i in students:
#     if i["marks"] > max:
#         max = i["marks"]

# print("Highest : ",max)

# for i in students:
#     if i["marks"] >= 80:
#         print(i["name"] , " : ", i["marks"])



# ------------------------------------------------
# numbers = [1, 2, 3, 4, 5, 6]
# square = {n : n * n for n in numbers}
# print(square)
# even = {i : i * i for i in numbers if i % 2 == 0}
# print(even)




#  _______________________________________________
#                 Function()
# _______________________________________________

# def welcom():
#     print("Welcome to python ")

# welcom()
# ------------------------------------------------



# def square(n):
#     return n * n

# result = square(5)
# print("square : ",result)
# ------------------------------------------------



# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# even = is_even(2)
# odd = is_even(5)
# print(even)
# print(odd)
# ------------------------------------------------


# def add(a , b):
#     return a + b

# addition = add(2, 4)
# print(addition)
# ------------------------------------------------


# def largest(a,b):
#     return max(a,b)

# large = largest(20,10)
# print("Largest : ", large)
# ------------------------------------------------


# def calculate(a ,b):
#     sum = a + b
#     mul = a * b

#     return sum , mul

# answer = calculate(10,20)
# print(answer)


# ------------------------------------------------
#               default parameter
# ------------------------------------------------

# def greet(name = "Guest"):
#     print("Hello ", name)

# greet()
# greet("Sanjana")

# def power(num , expo = 2):
    
#     print(num ** expo)

# power(5)
# power(5 , 3)


# ------------------------------------------------
#                   *args
#     if we dont know how many argumenats user send then used 
# ------------------------------------------------
# def total(*numbers):
#     print(sum(numbers))

# total(10, 20)
# total(10, 20, 30)
# total(1, 2, 3, 4, 5)
# ------------------------------------------------


# def find_max(*num):
#     print(num)
#     print("MAX : ", max(num))

# find_max(30,20)
# find_max(4,60,20)


# ------------------------------------------------
#           **kwargs
# ------------------------------------------------
# def show_details(**kwargs):
#     for key , value in kwargs.items():
#         print(key , " : ", value)
# ------------------------------------------------


# show_details(name = "sanja", age = 34 , course= "BCA")

# def student_info(name , *skills , **details):
#     print("Name : ", name)
#     print("Skills : ", skills)
#     for key , values in details.items():
#         print(key , " : ", values)

# student_info("sanjana", "py", "django", "js", age = 23 , city= "pune")
# ------------------------------------------------


# ------------------------------------------------
#           scope local , global , global keyword
# ------------------------------------------------
# c = 0
# def increase():
#     global c 
#     c = c + 1
#     print(c)

# increase()
# increase()
# increase()


# ------------------------------------------------
#           Lambda
# ------------------------------------------------

cube = lambda n : n * n * n
print(cube(3))

large = lambda a, b, c : max(a , b , c)
print(large(4,2,5))

