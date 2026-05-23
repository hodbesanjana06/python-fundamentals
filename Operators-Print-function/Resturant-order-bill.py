
'''

     RESTURANT BILL RECEIPT      
--------------------------------------------------
ITEM           QTY     PRICE     TOTAL     
--------------------------------------------------
Pizza          2       120       240       
Burger         1       60        60        
Pasta          1       100       100       
Cold Drink     3       40        120       
--------------------------------------------------
GRAND TOTAL =  520

'''


i1, i2 , i3 , i4 = "Pizza","Burger","Pasta","Cold Drink"
p1 , p2 , p3 , p4 = 120, 60, 100 , 40
q1 , q2 , q3 , q4 = 2, 1, 1, 3

t1 = p1 * q1
print(t1)
t2 = p2 * q2
t3 = p3 * q3
t4 = p4 * q4


print("     RESTURANT BILL RECEIPT      ")
print("-" * 50)

print(f"{'ITEM':<15}{'QTY':<8}{'PRICE':<10}{'TOTAL':<10}")
print("-" * 50)

print(f"{i1:<15}{q1:<8}{p1:<10}{t1:<10}")
print(f"{i2:<15}{q2:<8}{p2:<10}{t2:<10}")
print(f"{i3:<15}{q3:<8}{p3:<10}{t3:<10}")
print(f"{i4:<15}{q4:<8}{p4:<10}{t4:<10}")

print("-" * 50)

print("GRAND TOTAL = " ,t1 + t2 + t3 +t4)


