name = "pyahtone"
c =0
print(name)
print("revese : ", name[::-1])
print("_______________________________________")

for i in name:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        c += 1
        print(i)
    else:
        pass
print("Vowel Count : ", c)
print("_______________________________________")


lst = [12, 45, 2, 89, 34]
max = lst[0]
# print("Max : ", max(lst))
for i in lst:
    if i > max:
        max = i
    else:
        pass
print("Original List : ", lst)
print("Max : ",max)


print("_______________________________________")
name = "madamer"
print("Oriinal String...", name)
rev = name[::-1]
if name == rev:
    print("palindrom string...", rev)
else:
    print("not palindrom....", rev)


print("_______________________________________")
for i in range(1, 51):
    if   i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 :
        print("Fizz")
    else:
        print(i)

print("_______________________________________")
l1 = [1, 2, 2, 3, 4, 4, 5]
print("Original : ", l1)
s = set(l1)
l1 = list(s)
print("Remove Duplicate : ",l1)

print("_______________________________________")
l2 = [10, 20, 4, 45, 99]
sort= sorted(l2)
print(l2)
print("Second Largest : ",sort[-2])

print("_______________________________________")

d1 = {"a": 1 , "b": 2}
d2 = {"b": 3 , "c": 4}
d1.update(d2)
print(d1)

print("_______________________________________")

l3 = [1,2,3,4,6,7,8]
print(l3)
for i in range(1 , 9):
    if i in l3:
        pass
    else:
        print("Missing Number : ",i)
   

print("_______________________________________")

s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Anagram : ", s1,":", s2)
else:
    print("Not Anagram : ", s1,":", s2)


print("_______________________________________")
