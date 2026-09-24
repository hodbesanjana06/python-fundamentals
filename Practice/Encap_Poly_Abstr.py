from abc import ABC, abstractmethod


# class BankAccount:
#     def __init__(self, name , balance):
#         self.name = name
#         self.__balance = balance

#     def deposit(self, amt):
#         print("Bank Balance : ", self.__balance)
#         self.__balance = self.__balance + amt
#         print("Deposit amt : ",amt ,"| Total balance now : ",self.__balance)

#     def withdraw(self, amt):
#         self.__balance = self.__balance - amt
#         print("Withdraw amt : ",amt ,"| Total balance now : ",self.__balance)


#     def show_balance(self):
#         print("Total Balance : ",self.__balance)

# b1 = BankAccount("Sanajana", 5000)
# b1.deposit(1000)
# b1.withdraw(500)
# b1.show_balance()

# print(b1.name)



# class Employee:
#     def __init__(self , name , dept , salary):
#         self.name = name
#         self._dept = dept
#         self.__salary = salary

#     def display(self):
#         print(self.name , self._dept , self.__salary)

#     def update_salary(self , new_sal):
#         if new_sal > 100:
#             self.__salary =  new_sal
#         else:
#             print("Invalid salary : ", new_sal)

    

# e1 = Employee("sanjana", "IT" , 20000)
# # e1.display()

# e1.update_salary(90)
# e1.display()




# ___________________________________________________________
#       Polymorphism
# ___________________________________________________________

# class Dog:
#     def sound(self):
#         print("Dog is barking")

# class Cat:
#     def sound(self):
#         print("Cat is meowing")

# class Cow:
#     def sound(self):
#         print("Cow is mooing")

# d1 = Dog()
# d1.sound()

# c1= Cat()
# c1.sound()

# c2 = Cow()
# c2.sound()

# animal = [Dog() , Cat() , Cow()]

# for a in animal:
#     a.sound()


# ___________________________________________________________
#       Abstarction
# ___________________________________________________________

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def area(self, r):
#         s = r * r
#         print("Circle : ",s)

# class Rectangle(Shape):
#     def area(self , l , w):
#         r = l * w
#         print("Rectangle : ", r)

# c1 = Circle()
# c1.area(2)

# r1 = Rectangle()
# r1.area(2 , 3)

        


# ___________________________________________________________
#       Combined all 
# ___________________________________________________________
# class Student:
#     def __init__(self , name , age , marks):
#         self.name = name 
#         self.age = age
#         self.marks = marks

#     def display(self):

#         print("__________________________________")
#         print("Name : ", self.name)
#         print("Age : ", self.age)
#         print("Marks : ", self.marks)

#     def calculate(self):
#         s = sum(self.marks)
#         a = s / len(self.marks)
#         print("Total : ",s)
#         print("Average : ", a)

#     def passed(self):
#         s = sum(self.marks)
#         a = s / len(self.marks)

#         if a >= 40:
#             print("Passed")
#         else:
#             print("Failed")

# s1 = Student("sanjana", 23 , [20, 30, 40 ])
# s1.display()
# s1.calculate()
# s1.passed()


# s2 = Student("sanju", 43 , [290, 90, 140 ])
# s2.display()
# s2.calculate()
# s2.passed()

# ___________________________________________________________
class Employee:
    def __init__(self , name , salary , skills):
        self.name = name 
        self.salary = salary
        self.skills = skills

    def display(self):
        print("__________________________________")
        print("Name : ", self.name)
        print("Salary : ", self.salary)
        print("Skills : ", self.skills)


class Developer(Employee):
    def __init__(self , name , salary, skills , language):
        super().__init__(name , salary , skills)
        self.language = language

    def Work(self):
        print("Sanjana works with ", self.language)


class Tester(Employee):
    def __init__(self, name, salary, skills , tool):
        super().__init__(name, salary, skills)
        self.tool = tool

    def Work(self):
        print("Sanjana tests using ", self.tool)


d1= Developer("Sanjana", 20000 , ["py", "js", "recst"], "Pythoon")
d1.display()
d1.Work()



t1 = Tester("Rajiv", 70000 , ["py", "js", "recst"],  "VSVS")
t1.display()
t1.Work()

