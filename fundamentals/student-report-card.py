def student(name, age, city , m1 , m2 , m3):
    print("             Student-Report-Card         ")
    print("---------------------------------------------")
    print("Name : ", name)
    print("Age  : ", age)
    print("City : ", city, end="\n")
    print(end="\n")

    print("Maths", " | ", "Science", " | ", "English" )
    print( m1 , "    |  ", m2 , "     |  ", m3)
    
    t = m1 + m2 + m3
    a = t / 3
    print(end="\n")

    print("Total : ", t)
    print("Average : ", a)

    if a > 35:
        print("Result : ","Pass")
    else:
        print("Result : ","Fail")
    print("---------------------------------------------")



student("sanjana hodbe", 12, 'mumbai', 55, 53, 73)
# student("prajwal jagtap", 13, 'mumbai', 60, 43, 73)
