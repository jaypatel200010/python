# 36] How Do You Check The Presence Of A Key In A Dictionary?
dict1={1:'jay',2:4,3:'himanshu'}
# User input to enter the key to check
u_key = int(input("Enter key for the dictionary to check if it exists or not: "))
# Check if the key exists in the dictionary
if u_key in dict1:
    print("Key exists in the dictionary:")
else:
    print("Key does not exist in the dictionary:")