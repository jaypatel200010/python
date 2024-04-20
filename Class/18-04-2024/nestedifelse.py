#nested

n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))
n3 = int(input("Enter n3 : "))

if n1>n2:
    if n1>n3:
        print(n1, "Is greatest...!")
    else:
        print(n3, "is greatest...!")

else:
    if n2>n3:
        print(n2, "Is greatest...!")
    else: 
        print(n3, "Is greatest..!")