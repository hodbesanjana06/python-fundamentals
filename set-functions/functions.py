'''print("       1. Find the Square          ")

def square(n):
    print("Square of {} = ".format(n), n ** 2)

square(5)

'''


'''
print("         Evene or odd        ")
def check(n):
    if n % 2 == 0:
        print("Even: ", n)
    else:
        print("Odd: ", n)

check(1)
check(4)

'''


'''
print("    Maximum of Two Numbers        ")
def check(n1,n2):
    print("Max : ",max(n1,n2))

check(20,10)

'''



'''
print("         find Area           ")
def area(l,w):
    print("Area is : ", l*w)

area(8,5)

'''


'''
print("         Simple Intrest       ")
def Count(p,r,t):
    print("Principle :", p, " ROI :", r,"%", " Time :",t)

    r= p * r /100 * t
    print("Simple Interest : ",r)

Count(1000, 5 , 2)

'''



'''print("     Sum of Digit        ")
def sum(n):
    s=0
    while n > 0:
        r = n % 10
        s = s + r
        n = n // 10

    return s

s=sum(456)
print(s)

'''
'''

print("         max & min with return     ")
def check(n1,n2,n3,n4,n5):
    b = max(n1,n2,n3,n4,n5)
    s = min(n1,n2,n3,n4,n5)

    return b,s
r=check(20,10,4,1,6)
print(r)
'''

'''
def count(name):
    v=0
    c=0
    for i in name:
        if i in 'aeiou':
            v +=1
        else:
            c += 1

    return v,c

s=count('python')
print(s)
'''


# ____________________LAMBDA FUNCTION_____________________________
'''
a = (lambda a,b : a if a > b else b)(20,15)
print("MAX : ",a)

'''


# ____________________Default Arguments_____________________________
'''
def greet(name='Guest'):
    print("Hello ", name)

greet()
greet('sanjana')

'''


'''
print("     Power of num        ")
def power(b,e=2):
    print("base^exponent", b ** e )

power(5)
power(5,3)

'''

# ____________________ Arbitrary Arguments (*args)_____________________________
'''

print("     sum of number       ")
def sum(*args):
    sum=0
    for i in args:
        sum = sum + i
    print(sum)
sum(1 ,2, 3, 4, 5)

'''


'''
print("     Largest num        ")
def check(*args):
    print("Max : ",max(args))

check(8 ,15 ,3 ,27 ,10)

'''

'''
print("         Count Arguments         ")
def check(*args):
    print("Count of passed elements : ", len(args))

check(10 ,20 ,30 ,40)

'''


# ____________________ Keyword Arguments (**kwargs)_____________________________

'''
print("     Student Details     ")

def display(**kwargs):
    print(kwargs, sep=":")

display(name='sanjana', age=20, city="Pune")

'''
'''
print("         marks total         ")

def count(**kwargs):
    t=0

    for key ,value in kwargs.items():
        t += value

    print("TOTAL", t)

count(math=90, sience = 85, english=80)

'''


# ____________________ Mixed Practice_____________________________
'''
print("         Employee salary         ")

def salary(s,b=5000):
    print("Total salary : ", s+b)

salary(25000)

'''

'''
print("     Shopping bill       ")
def bill(*args):
    print("Prices : ", args)
    t=0
    for i in args:
        t += i

    return t

ans = bill(100 ,250 ,50 ,300)
print("Total Bill ",ans)


'''

'''
print("         Calculator          ")

def cal(n1,n2):
    sum = n1 + n2
    dif = n1 - n2
    pro = n1 * n2
    quo = n1 / n2

    return sum , dif, pro , quo

ans = cal(20,5)
print(ans)

'''


'''
lst = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8]
l = list(filter(lambda  x:  x % 2 == 0, lst))
print(l)

'''

print("     Function Combination Challenge      ")
def mix(*args, multi=3):
    t=0
    add = 0
    for i in args:
        t = i * multi
        add = add + t

    return add

r = mix(1 ,2 ,3 ,4)
print(r)