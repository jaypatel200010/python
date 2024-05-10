# Write python program that swap two number with temp variable and without temp variable.

# Take input from the user
n1 = int(input("enter num 1 : "))
n2 = int(input("enter num 2 : "))

# Swapping using a temp var
print("using temp")


print("BEFORE SWAPPING")

print("value of n1 = ", n1)
print("value of n2 = ", n2)

# Swapping using a temp var
temp = n1
n1 = n2
n2 = temp



print("AFTER SWAPPING")
print("value of n1 = ", n1)
print("value of n2 = ", n2)



# Swapping without using a temp var
print("SWAPPING WITHOUT TEMP")


print("BEFORE SWAPPING")

print("value of n1 = ", n1)
print("value of n2 = ", n2)

# Swapping without using a temp var
n1, n2 = n2, n1


print("AFTER SWAPPING")

print("value of n1 = ", n1)
print("value of n2 = ", n2)