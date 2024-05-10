# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

# Take input from the user for three numbers
n1 = int(input("ENTER NUMBER 1 : "))

n2 = int(input("ENTER NUMBER 2 : "))

n3 = int(input("ENTER NUMBER 3 : "))


# Check if any two numbers are the same
if n1 == n2 or n2 == n3 or n1 == n3:
    print("ANY TWO OF THE ENTERED NUMBERS ARE THE SAME, SO SUM CAN'T BE DONE")
    print("SUM = 0")
    

# If all three numbers are different, calculate their sum
else:
    print("SUM OF ALL THREE GIVEN NUMBERS IS = ", n1 + n2 + n3)
  