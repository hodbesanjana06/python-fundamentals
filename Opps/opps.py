'''print("     Create a Student Class sho info          ")
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name : ", self.name, "Age : ", self.age)



s= Student('alica', 21)
s.display_info()



'''
'''
print("     find area & perimeter       ")

class Rectangle:
    def __init__(self, l , w):
        self.l = l
        self.w = w

    def area(self):
        print("Area : ",self.l * self.w)

    def perimeter(self):
        print("Perimeter: ",2*(self.l+self.w) )

r = Rectangle(5,3)
r.area()
r.perimeter()

'''

'''
print("     Bank Account        ")
class BankAccount:
    t=0
    def deposit(self, amt):
        
        self.t = self.t + amt

    def withdraw(self, amt):
        w=0
        if self.t < amt:
            print("not sufficeient balance..")
        else:
            self.t = self.t - amt
            print("Withdraw :", amt)

    def balance(self):
        print("Total balance : ",self.t)

b = BankAccount()
b.deposit(1000)
b.balance()
b.withdraw(200)
b.balance()


'''
'''
print("         Car Details         ")

class Car:

    def __init__(self, brand,year, model):
        self.brand = brand
        self.year = year
        self.model = model

    def start_engine(self):
        print(" | Brand : ", self.brand, " | Model : ", self.model, " | Year : ", self.model)

c = Car('sanjana','yashwant', 2006)
c2= Car('radha', 'krishna', 2007)
c2.start_engine()
c.start_engine()

'''

'''
print("     Inheritance: Person → Teacher       ")

class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age


class Teacher(Person):

    def __init__(self, name,age,subj):
        self.subj = subj
        self.name = name
        self.age = age

    def show(self):
        print(" | Name :", self.name, " | Age :",self.age, " | subject :", self.subj)

t1 = Teacher('rahul',  45, 'DSA')
t2 = Teacher('english', 55, 'python')
t2.show()
t1.show()

    '''



'''
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
       print("Dog Says Woof")

class Cat(Animal):
    def make_sound(self):
        print("Cat Says Meow")

d = Dog()
c = Cat()
d.make_sound()
c.make_sound()

'''