#and operator
#or operator

n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))
n3 = int(input("Enter n3 : "))

if n1>n2 and n1>n3:
    print(n1, "IS grestest")

elif n2>n1 and n2>n3:
    print(n2, "Is greatest")

else:
    print(n3, "Is greatest")