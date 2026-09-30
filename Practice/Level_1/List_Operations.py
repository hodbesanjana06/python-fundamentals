# -----------------------------------------------

# def duplicate(numbers):
#     new = set(numbers)
#     return list(new)

# def find(numbers):
#     new = duplicate(numbers)
#     sort = sorted(new)
#     print("Seconde largest : ",sort[-2])

# def calculate(numbers):
#     total = 0
#     # for i in numbers:
#     #     total = total + i
#     # print("Total : ", total)
#     print("Total : ", sum(numbers))
#     print("Average : ", sum(numbers) / len(numbers))

def duplicates(numbers):
    seen = set()
    duplicate = set()

    for i in numbers:
        if i in seen:
            duplicate.add(i)
        else:
            seen.add(i)
    return duplicate


numbers = [10, 20, 10, 30, 40, 20, 50, 60]
# print("Original List : ", numbers)
# print("Remove duplicates : ",duplicate(numbers))
# find(numbers)
# calculate(numbers)
print(duplicates(numbers))