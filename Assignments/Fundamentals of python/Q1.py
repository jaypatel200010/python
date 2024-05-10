# Write a Python program to check if a number is positive, negative or zero.

# input from the user
num = int(input("ENTER NUMBER : "))

# Check for zero
if num == 0:
    print("**ENTERED NUMBER IS ZERO**")

# Check for +ve
elif num > 0:
    print("**ENTERED NUMBER IS POSITIVE**")

# check for -ve
else:
    print("**ENTERED NUMBER IS NEGATIVE**")