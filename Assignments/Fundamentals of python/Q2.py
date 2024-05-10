# Write a Python program to get the Factorial number of given number.

# input from the user
num = int(input("ENTER A NUMBER : "))

# Check for -ve
if num < 0:
    print("ENTERED NUMBER IS NEGATIVE")
else:
    # Initialize factorial variable to 1
    fact = 1
    
    # Calculate factorial using a loop
    for i in range(1, num + 1):
        fact = fact * i
    
    # Print the factorial of the given number
    print("FACTORIAL IS : ", fact)