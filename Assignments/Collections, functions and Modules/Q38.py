#Write a Python program to check multiple keys exists in a dictionary
# Define the dictionary
dict = {1: 'jay', 2: 'patel', 3: 'Uday', 4: 'tushar', 5: 'himanshu'}

# Keys to check
check = [1, 4, 6]

# Check if each key exists in the dictionary
for key in check:
    if key in dict:
        print(f"The key '{key}' exists in the dictionary.")
    else:
        print(f"The key '{key}' does not exist in the dictionary.")