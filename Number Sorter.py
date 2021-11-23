#Number Sorter
#Create a program that ask 4 numbers. 
#Print the 4 numbers from highest to lowest using only if-else statement.

a = float(input("The 1st digit is: "))
b = float(input("The 2nd digit is: "))
c = float(input("The 3rd digit is: "))
d = float(input("The 4th digit is: "))

if a > b and a > c and a > d:
    if b > c and b > d and c > d : 
        print(f"The order is {a,b,c,d}")
    else:
        print(f"The order is {a,c,b,d}")
elif b > a and b > c and b > d:
    if a > c and a > d and c > d :
        print(f"The order is {b,a,c,d}")
    else:
        print (f"The order is {b,c,a ,d}")
elif c > a and c > b and c > d:
    if a > b and a > b and b > d:
        print (f"The order is {c,a,b,d}")
    else:
        print (f"The order is {c,b,a,d}")
else:
    if d > a and d > b and d > c and a > b and a > c and b > c:
        print(f"The order is {d,a,b,c}")
    else:
        print(f"The order is {d,b,a,c}")

print ("Done")
    