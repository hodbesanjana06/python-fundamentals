
# print the vowels and count
'''
text = " The Quick Brown Fox Jumps ever the lazy dog "
c = 0
for i in text:
    if i == "a" or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        print(i)
        c = c+ 1
   
print("Vowel Count = ", c)
'''


# palindrom string or not
'''name = input("Enter name : ")

if name == name[::-1]:
    print("Palindrom string")
else:
    print("No Palindrom")
    
'''

# Convert Lowercase to Uppercase using ord() and chr()

'''l = 'a'
u = "S"
print("Uppercase of a : ", chr(65))
print("Lowercase of S : ", chr(115))
'''

# Create Characters from ASCII 65, 97, 122
'''print("ASCII of 65 :", chr(65))
print("ASCII of 97 :", chr(97))
print("ASCII of 122 :", chr(122))
'''

# Check Pangram

'''name ="sanja^7na"
print("NAME : ", name)
if name.isalpha():
    print("contain alphabets")
else:
    print("other symbols")
    
'''

# Count Special Characters
'''
name = "s@n#j@n@"
print("Original Text : ", name)
c= 0
for i in name:
    if i.isalpha():
        pass
    else:
        c += 1

print("Special characters : ", c)

'''

# Replace Every Character with Next Alphabet
'''name = 'abce'
r = ''
print("NAME : ", name)
for i in name:
    r += chr(ord(i) +1)
print(r) '''   


# Remove Duplicate Characters
'''
name = "programming"
print("Original : ", name)
s = set(name)
print("After remove the duplicates : ","".join(s))

'''

# Longest Word in Sentence
'''
name ="sanjana yashwant hodbe"
print(name)
n1 = name.split()
print(n1[0], ":", len(n1[0]))
print(n1[1], ":", len(n1[1]))
print(n1[2], ":", len(n1[2]))
print("Max : ", max(n1[0], n1[1], n1[2]))
'''

#. Capitalize First Letter of Every Word
'''name = "capitalized first letter of every word" 
print(name.title())

'''

# Name   Marks
# Ram    90
# Shyam  85
'''
print("Name", "Marks")
print(f"{'Name':<10} {'Marks':<10}")
print(f"{'Ram':<10}", 90)
print(f"{'Shyam':<10}", 80)

'''

# Format Name and Age
'''
name , age =  'Rahul', 32
print("My name is {} and i am {} years old".format(name, age))

'''

# Swap First and Last Character
'''name = "SanjanA"
r = name[-1] + name[1:-1] + name[0]
print(name,"-->",r)

'''

# Find Last Character Without Using [-1]
name = "sanjana"
print(name ,"--->", name[len(name) -1])