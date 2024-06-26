# Write a Python program to get the Fibonacci series of given range.

print()
num = int(input("Enter the maximum value for Fibonacci series: "))
# assigning the first two numbers in the Fibonacci sequence
a, b = 0, 1

# Fibonacci sequence up to the maximum value
while a <= num:
    print(a, end=" ")  #current Fibonacci number
    a, b = b, a + b    # Update the Fibonacci sequence (next Fibonacci number)

    # Break the loop if the next Fibonacci number exceeds the maximum value
    if a > num:
        break
print()  # Move to the next line after printing the series