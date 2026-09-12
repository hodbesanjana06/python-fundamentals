# students = [
#     {
#         "name": "Sanjana",
#         "age": 23,
#         "course": "Python",
#         "marks": [85, 78, 90],
#         "skills": ("Python", "Django", "React")
#     },
#     {
#         "name": "Rahul",
    
#         "age": 22,
#         "course": "Python",
#         "marks": [70, 88, 75],
#         "skills": ("Python", "JavaScript")
#     },
#     {
#         "name": "Priya",
#         "age": 24,
#         "course": "Django",
#         "marks": [92, 95, 89],
#         "skills": ("Python", "Django", "React")
#     }
# ]

# def display_students():
#     for i in students:
#         print("Name : ", i["name"])
#         print("age : ", i["age"])
#         print("Course : ", i["course"])
#         print("Marks : ", i["marks"])
#         print("Skills : ", i["skills"])
#         print("_________________________________")
# display_students()


# def calculate_marks(marks):
#     t = 0

#     for i in marks:
#         t = t + i
#         a = t/len(marks)
#         if a >= 80:
#                 print("Above 80 : ",students[0]["name"])
        
#     print("Total : ",t)
#     print("Average : ", a)

    
# calculate_marks(students[0]['marks'])


# def add_students(name , age , course="python"):
#     student ={
#         "name" : name ,
#         "age" : age ,
#         "course" : course,
#         "marks" : [],
#         "skills" : ()
#     }
#     students.append(student)

# add_students("shravni", 34)
# print(students)


# ___________________________________________________________
name = "Sanjana"
age = 23
skills = ["Python", "Django", "React", "JavaScript"]
marks = (85, 78, 90, 88)

# def display_name(name):
#     print(name.upper())

# display_name(name)
# ___________________________________________________________

# def display_skills(*args):
#     for i in args:
#         print(i)

# display_skills(*skills)

# ___________________________________________________________
# def calculate_marks(*marks):
#     t= 0
#     for i in marks:
#         t = t + i
#     a = t / len(marks)
#     print("Total ", t)
#     print("Avreage : ", a)

# calculate_marks(*marks)


# ___________________________________________________________
# extra_skills = ["Python", "HTML", "CSS", "React"]
# first_skill = set(extra_skills)
# second_skill = set(skills)
# print("Common skills : ",first_skill & second_skill)
# print("unique skills : ",first_skill | second_skill)


# ___________________________________________________________
# employee = {
#     "name": "Sanjana",
#     "age": 23,
#     "course": "BCA"
# }
# employee["city"] = "pune"
# employee["experience"] = "Fresher"
# for key , values in employee.items():
#     print(key , " : ", values)

# ___________________________________________________________
#       LIST COMPREHENSION ?
numbers = [1, 2, 3, 4, 5]
result = [n * n for n in numbers]
print(result)


# ___________________________________________________________
# result = tuple(filter(lambda x : x > 80 , marks))
# print(result)


# ___________________________________________________________
# def employee_details(**details):
#     for key , values in details.items():
#         print(key , " : ", values)

# employee_details(name= "sanjana", age= 23 , city = "pune", role="Developer")

def employee_report(name , *skills , **details):
    print("name : ", name)
    print("Skills : ", skills)
    for key , values in details.items():
            print(key , " : ", values)

employee_report("sanjana", "python", "Django", "React", age = 34 , city = "pune")