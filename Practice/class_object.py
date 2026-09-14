# class Student:

#     def __init__(self , name , age , course):
#         self.name = name
#         self.age = age
#         self.course = course

#     def shows(self):
#         print(self.name , self.age , self.course)


# s1 = Student("disha", 23 , "BCA")
# s2 = Student("Sanjana", 45 , "Nothing")
# s1.shows()
# s2.shows()



# ___________________________________________________________
#                   INHERRITANCE
# ___________________________________________________________
class Employee:

    def __init__(self , name , salary):
        self.name = name 
        self.salary = salary

   

class Devloper(Employee):
    def __init__(self, language, name , salary):
        super().__init__(name , salary)
        self.language = language

    def display(self):
            print("NAME : ", self.name)
            print("SALARY : ", self.salary)
            print("Language : ", self.language)


d1 = Devloper("sanjana", 34444 , "dkadj" )
d1.display()

    