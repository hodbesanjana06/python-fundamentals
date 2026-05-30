'''print("     Count Unique Elements       ")

s={1, 2 ,3 ,2 ,1 ,4 ,5 ,4}
print(s)
print("Unque element count : ",len(s))
'''

'''
print("     Union of two sets       ")

s1 = {10 ,2 ,3 ,4}
s2 = {3 ,4 ,50 ,6 ,7}
r=s1.union(s2)
s=sorted(r)
print(set(s))

'''

'''
print("     Intersection  of two sets       ")

s1 = {10 ,2 ,3 ,4}
s2 = {3 ,4 ,50 ,6 ,7}
print(s1,s2)
r=s1.intersection(s2)
# print(r)
s=sorted(r)
print(set(s))

'''

'''
print("     Diffrence  of two sets       ")

s1 = {1 ,2 ,3 ,4,5}
s2 = {2,4,6}
print(s1,s2)
r=s1.difference(s2)
print(r)

'''


'''
print("     Symmetric  of two sets       ")

s1 = {1 ,2 ,3 ,4}
s2 = {3,4,6,5}
print(s1,s2)
r=s1.symmetric_difference(s2)
print(r)

'''



'''
print("     subset  of two sets       ")

s1 = {1 ,2 ,3 ,4}
s2 = {3,4,1,2,3}
print(s1,s2)
r=s1.issubset(s2)
print(r)

'''

'''

print("     dis_joint  of two sets       ")
# two sets have no common elements.'
s1 = {1 ,2 ,3 ,4}
s2 = {5,7,8}
print(s1,s2)
r=s1.isdisjoint(s2)
print(r)

'''

'''print("         common characters       ")
name = "programming"
name2 = "gaming"

new =""

for i in name:
    if i in  name2 and i not in new:
        new += i
    else:
        pass

print(new)

'''

'''
print("         Unique Words Count          ")
name = "the cat and the dog and the cat"
s= name.split()
r= set(s)
print(r)
print("Count is : ", r)

'''


print("     Missing Numbers         ")
n=10
arr=[1,2,4,5,7,8,9]
print(arr)
print("Missing values ")
for i in range(1, n+1):
    if i not in arr:
        print(i)