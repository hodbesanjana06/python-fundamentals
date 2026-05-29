'''
print("         Sum of Tuple Elements           ")
t = (1,2,3,4,5)
print(t)

sum = 0
for i in t:
    sum += i

print("Sum of tuple : ", sum)

'''




'''
print("      Maximum and Minimum in Tuple       ")
t = (10, 20 ,1, 3, 56)
print("MAX : ",max(t))
print("MIN : ",min(t))

'''




'''
print("     Count Occurrences       ")

t = (2, 1, 2, 1, 3, 6, 3,6)
c=()
for i in t:
    if i in c:
        c[i]=1
    else:
        c [i] =+  1

print(c)

'''



'''
print("     reverse the tuple       ")
t = (4, 2, 3, 1, 4,6)
print("Original : ", t)
print("Reverse : ",t[::-1])

'''




'''
print("     Tuple Slicing       ")
t=(1,3,1, 3,5,7,54)
print("Original tuple : ", t)
print("first hlaf : ", t[0:4])
print("second half : ",t[4:])
'''




'''
print("     Remove Duplicates       ")
t=(1,3,1, 3,5,7,54)
new = []
for i in t:
    if i not in new:
        new.append(i)
    else:
        pass
print("original : ", t)
print("Remove duplicates : ",tuple(new))

'''




'''
print("     Swap 1st & last element        ")
t=(10, 20 ,20 ,40 ,50)
print("Original : ", t)

l = list(t)

last=l[0]
first=l[-1]

l[-1]=last
l[0]=first

print("Swapping : ",tuple(l))

'''




'''
print("     Index of element        ")
t = (10,20, 30, 40)
print("original : ", t)
c= int(input("Enter the number for indexing : "))

if c in t:
    print("index is ",t.index(c))
    print("Value present in tuple")
else:
    print("not valid ")

'''




'''
print("     Even and Odd Indexed Elements       ")

t=(10, 4, 20, 5, 3, 1, 40)
print("Original : ", t)
e=[]
o=[]
for i in t:
    if i % 2 == 0:
        e.append(i)
    else:
        o.append(i)

print("Event elelments : ", tuple(e))
print("Odd elelments : ", tuple(o))


'''





'''
print("     Tuple Packing and Unpacking     ")
t=(10, 4, 20, 40)
a,b,c,d=t
print("Unpacking into the variables : ", "a: ",a, " b:",b , " c :", c, " d :", d)

'''





'''
print("     Second Largest Element      ")
t=(10, 4, 20, 40)
s= sorted(t)
print(s)
print("Second largest : ", s[-2])

'''




'''
print("     Tuple to Dictionary         ")
k=("apple",'banana','mango')
v=(100,200,300)

new = dict(zip(k,v))
print(new)


'''



'''
print("     Common Elements in Two Tuples       ")
t1= (1,2,3,4,5)
t2 = (5,4,6,7,3)

s1=set(t1)
s2=set(t2)

common = s1 & s2
print("Common element : ",tuple(common))

'''



'''
print("         Merge and Sort Tuple        ")
t1= (1,8,3)
t2 = (5,4)
print(t1, "  ", t2)

merge = t1 + t2
print("Merge two tuples : ",merge)

sort= sorted(merge)
print("Sorted tuple : ", tuple(sort))
'''



'''
print("         square of number        ")
t=(1,2,3,4)
for i in t:
    print(i ** 2, end=" ")
    
'''