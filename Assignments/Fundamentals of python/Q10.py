# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

# Take input from the user for two integers
n1 = int(input("ENTER FIRST INTEGER : "))

n2 = int(input("ENTER SECOND INTEGER : "))


# Check if the two numbers are equal
if n1 == n2:
    print(True)
    

# Check if the sum of the two numbers is 5
elif n1 + n2 == 5:
    print(True)
   

# Check if the absolute difference between the two numbers is 5
elif abs(n1 - n2) == 5:
    print(True)
   

# If none of the above conditions are met, print False
else:
    print(False)
    