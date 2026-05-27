'''print("     Find Maximum Element        ")
l = [2, 3, 1, 6, 4]
print(l)
print(max(l))
m = 0
for i in l:
    if i > m:
        m = i

print("max : ", m)
print("min", min(l))

'''

'''
print("     Sum of Elements         ")
l = [3, 1, 3, 4, 5]
s = 0
for i in l:
    s += i

print("Sum : ", s)

'''
'''
print("         Count Even Numbers          ")
l = [3, 1, 6, 4, 5, 8, 9]
c=0
for i in l:
    if i % 2 == 0:
        c +=1
print(l)
print("Count even numbers : ", c)

'''


'''
print("         Reverse the list        ")
l = [3, 1, 6, 4, 5, 8, 9]
print("Original : ", l)
print("Reverse : ",l[::-1])

'''

'''
print("         Second Largest Element          ")
l = [3, 1, 6, 4, 5, 0, 9]
l.sort()
print(l)
print("Largest : ", l[-1])
print("Second Largest : ", l[-2])


'''

'''
print("         Remove Duplicate        ")
l = [3, 1, 3, 4, 5, 1, 9]
print("Original : ", l)
l= set(l)
print("Remove Duplicates : ",list(l))

'''


'''
print("     Rotate List by One Position to last        ")
l = [3, 1, 3, 4, 5, 1, 9]
print("Original : ", l)
last = l[-1]
l[-1]=l[0]
l[0]=last
print("After Moving : ",l)

'''

'''
print("         Frequency of an Element         ")
l = [3, 1, 3, 4, 5, 1, 9]
f = int(input("Enter element : "))
c = 0

for i in l:
    if i == f:
        c += 1
    else:
        pass
print("frequency of {} = ".format(f), c)


'''


# 2-D List / Matrix Practice

print("         Matrix Addition         ")
l = [1,2,3,4,5]
l2 = [1,2,3,7,5]
print("Original matrix : ", l , l2)
r = []
for i in range(len(l)):
    r.append(l[i] + l2[i])

print("Addition : ",r)