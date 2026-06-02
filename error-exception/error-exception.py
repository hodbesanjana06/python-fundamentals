'''

print("     divisible by zero       ")
try :
    n = int(input("Enter Number : "))
    d = int(input("Enter denomeinator : "))

    r = n /d

    print("Ressult : ", r)

except ZeroDivisionError:
    print("can not divisible by zero...")

'''


'''
print("     valuerror exception         )
try:
    num = int(input("Enter Number : "))
    print("you enterd : ", num)
except ValueError:
    print("Invalid input....")
    
'''



'''
lst = [10,20,30,40]
try:
    n = int(input("Enter index : "))
    print(lst[n])

except ValueError:
    print("Invalid idexd value ...")

except IndexError:
    print("Index is out of range...")
    
'''



'''
try:
    with open("sample.txt", "r") as f:
        print(f.read())

except FileNotFoundError:
    print("file not found")
    
'''


'''try:
    n1 = int(input("Enter first number : "))
    n2 = int(input("Enter second number : "))
    ch = input("Enter operation (+, - , * , % , /)")

    if ch == '+':
        print("addition : ", n1 + n2)
    elif ch == '-':
        print("substraction : ", n1 - n2)
    elif ch == '*':
        print("multiplication : ", n1 * n2)
    elif ch == '%':
        print("modulation : ", n1 % n2)
    elif ch == '/':
        print("division : ", n1 / n2)
    else:
        raise ValueError("Invalid operation...")
    
except ZeroDivisionError:
    print("can not divisible by zero try again...")

except ValueError as e:
    print(e)
    
'''


'''

def get_element(lst,i):
    try:
        return lst[i]
    except IndexError:
        return "Index out of range..."
    
lst = [10,20,30]

print(get_element(lst, 1))
print(get_element(lst, 10))

'''
pin=123
while True:
    try:
        n = int(input("Enter login num : "))
    except ValueError:
        print("invalid input...")
    else:
        if n == pin:
            print("Valid number entered : ", n)
            break
        else:
            print("Try Again....")
        
    finally:
        print("-----------------------")