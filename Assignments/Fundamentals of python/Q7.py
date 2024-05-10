# Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

# Take input from the user
n1 = int(input("ENTER A NUMBER : "))



# Check for zero
if n1 == 0:
    print("ENTERED NUMBER IS ZERO")
  
    
# Check for even
elif n1 % 2 == 0:
    print("ENTERED NUMBER IS EVEN")
   

# for odd
else:
    print("ENTERED NUMBER IS ODD")
    