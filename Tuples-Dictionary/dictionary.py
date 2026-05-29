'''
print("     Sum of Values       ")
dict = {
    "one":1,
    "two":2,
    "three":3
}
sum = 0

for i in dict:
    sum = sum + dict[i]

print(sum)

'''




'''
print("     Find Key by Value       ")
dict = {
    "one":1,
    "two":2,
    "three":3
}
for i in dict:
    print(i , dict[i])
    
'''




'''
print("         Max Value        ")
dict = {
    "one":1,
    "two":20,
    "three":3
}

# for i in dict:
print("Max value is : ",max(dict.values()))

'''



'''
d1= {"a":10, "b": 20, "c":30}
d2= {"d":10, "b": 20, "y":50}

r = d1.copy()

for key , value in d2.items():
    if key in r:
        r[key] += value
    else:
        r[key] = value

print(r)

'''



'''
print("     Remove Key      ")
d1= {1:10,  2: 20, 3:30}
print("original : ", d1)

c = int(input("Enter key for remove: "))


if c not in d1:
    print("not exits")
else:

    print("remove item : ",d1.pop(c))
    print("After remove : ",d1)

'''



'''
d1= {"a":10, "b": 20, "c":30}

swap = {}

for key , value in d1.items():
    swap[value]=key

print(swap)        
'''



'''
print("     Common Keys     ")

d1= {"a":10, "b": 20, "c":30}
d2= {"d":10, "b": 20, "c":50}

for i in d1:
    if i in d2:
        print(i, d1[i])
        
        
'''


'''
d1= {2:10,  1: 20,  5:30}
print(dict(sorted(d1.items())))

'''



'''
d1= {2:10,  1: 20,  5:30}
print("Length : ",len(d1))

'''



'''
print("         Student Marks            ")
s= {
    
    "Amit": 45,
    "Riya": 78,
    "John": 50,
    "Sara": 90,
    "Vikram": 35
}

for name , marks in s.items():
    if marks > 50:
        print(name , marks)
        
'''