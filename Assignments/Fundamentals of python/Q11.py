# Write a python program to sum of the first n positive integers.

# Take input from the user for a positive number

n = int(input("PLEASE ENTER A POSITIVE NUMBER = "))


# Assigning total sum 0 initially
total = 0

# Loop through positive integers up to the input number and calculate their sum
for i in range(1, n + 1):
    total += i

# Print the sum of the first 'num' positive integers
print(f"SUM OF THE FIRST {n} POSITIVE INTEGERS IS: {total}")
