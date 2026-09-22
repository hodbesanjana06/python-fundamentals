
# ___________________________________________________________
#             SIMPLE  INHERRITANCE
# ___________________________________________________________

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print("name : ", self.name)
#         print("Animal is eating")

# class Dog(Animal):
#     def bark(self):
#         print("Dog is Barking..")


# d1 = Dog("sheru")
# d1.eat()
# d1.bark()




# ___________________________________________________________
#        MULTIPLE  INHERRITANCE
# ___________________________________________________________

# class Father:
#     def show_father(self):
#         print("Father : Engineer")

# class Mother:
#     def show_mother(self):
#         print("Mother : Teacher")

# class Child(Father , Mother):
#     pass

# c1 = Child()
# c1.show_father()
# c1.show_mother()



# ___________________________________________________________
#        Multilevel  INHERRITANCE
# ___________________________________________________________
# class Vehicle:
#     def show_vehicle(self):
#         print("Vehicle can move")

# class Car(Vehicle):
#     def show_car(self):
#         print("Car has 4 wheels")

# class SportsCar(Car):
#     def show_sportcar(self):
#         print("Sports car is fast")


# s1 = SportsCar()
# s1.show_vehicle()
# s1.show_car()
# s1.show_sportcar()



# ___________________________________________________________
#        Hierarchical  INHERRITANCE
# ___________________________________________________________
# class Employee:
#     def show_employee(self):
#         print("Employee works in a company")

# class Developer(Employee):
#     def write_code(self):
#         print("Developer writes code")

# class Tester(Employee):
#     def test_software(self):
#         print("Tester Tests Software")

# d1 = Developer()
# t1 = Tester()

# d1.show_employee()
# d1.write_code()

# t1.show_employee()
# t1.test_software()



# ___________________________________________________________
#       Combined
# ___________________________________________________________
class Empoyee:
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary

    def display_emp(self):
        print("Name : ", self.name)
        print("Salary : ", self.salary)

class Developer(Empoyee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def write_code(self):
        print(self.language , "is the language .")

class Tester(Empoyee):
    def __init__(self, tool):
        self.tool = tool

    def test(self):
        print("Tool : ",self.tool)


class SeniorDeveloper(Developer):
    def __init__(self ,exp):
        self.exp = exp

    def show_experience(self):
        print("Experience : ", self.exp)


d1 = Developer("sanjana", 20000, "py")
d1.display_emp()
d1.write_code()

t1 = Tester("VS")
t1.test()



s1 = SeniorDeveloper("1 year")
s1.show_experience()

       