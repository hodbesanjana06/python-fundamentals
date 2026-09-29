def total(marks):
    t= 0
    for i in marks:
        t = t + i
    return t

def average(marks):
    t1=0
    for i in marks:
        t1 = t1 + i
    a = t1 /len(marks)

    return a


def ispass(marks):
    t1=0
    for i in marks:
        t1 = t1 + i
    a = t1 /len(marks)

    if a > 35:
        print("PASS")
    else:
        print("Fail")
