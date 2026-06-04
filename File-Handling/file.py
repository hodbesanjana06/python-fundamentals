'''# import os

# print("Current folder :", os.getcwd())
with open("notes.txt", "w") as f:
    f.write("Hey this is the file handling section \n ")
    f.write("Create File name Notes.txt \n")
    f.write("write some contend in it")

print("Write successfully....")

'''


'''

print("         Read a File         ")
with open("notes.txt","r") as f:
    text = f.read()

print(text)

'''

'''
print("     Count numbers of lines      ")
with open("notes.txt","r") as f:
    count = f.readlines()

print("Total lines ", len(count))

'''


'''
print("    Count Number of Words         ")
with open("notes.txt", 'r') as f:
    c = f.read()
con = c.split()
print("Total Words : ", len(con))

'''


'''
print("        Append Data           ")

text = input("Enter data for append : ")

with open("notes.txt", 'w')as f:
    f.write(text)

print("text append sucessfully......")

'''

'''
print("     Copy Contents of One File to Another        ")

with open("notes.txt", 'r') as f:
    data = f.read()

with open("second.txt", 'w') as f1:
    f1.write(data)

print("file copy sucessfully...")

'''

'''
print("     Search a Word in a File     ")

s = input("Enter the word for searching : ")

with open("notes.txt", 'r') as f:
    content = f.read().lower()

c = content.count(s.lower())

print(f"{s} found {c} times")

'''

'''print("     replace the words       ")
old_word = input("word to replace : ")
new_word = input("New word : ")

with open("notes.txt", 'r') as f:
    txt = f.read()

txt = txt.replace(old_word, new_word)

with open("notes.txt", 'w')as f:
    f.write(txt)

print("replce ....")

'''


'''
print("     Store Student Records       ")

name = input("Enter name : ")
m = int(input("Enter marks : "))

with open("notes.txt", 'w') as f:
    f.write("Name :  {} \n Marks :  {}".format(name, m))

print("Added .....")

'''
'''
print("     count employee salary in csv file       ")
import csv, os

# print("Current file : ",os.getcwd() )
# print(os.listdir())

t = 0
c = 0

with open("emp.csv", "r") as f:
    txt = csv.DictReader(f)

    for i in txt:
        t += int(i['Marks'])
        c += 1

print("Average is : ", t // c)


'''


print("     Total lines - Total words - Total characters - Most frequent word       ")

from collections import Counter

with open("notes.txt", "r") as f:
    content = f.read()

lines = content.splitlines()
words = content.lower().split()
word_c = Counter(words)
most_common_word, frequency = word_c.most_common(1)[0]

print("Total Lines : ", len(lines))
print("Total Words : ", len(words))
print("Characters : ",len(content))
print("MOst frequency words : ", most_common_word)
print("Frequency : ", frequency)