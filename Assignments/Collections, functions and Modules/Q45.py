# 45] Write a Python program to find the highest 3 values in a dictionary.
dict1 = {'jay':7,'himanshu':75,'tushar':111,'ketan':21}
print("dictionary = ",dict1)
# Sort the values of the dictionary in ascending order and assign it to the variable dict
dict = sorted(dict1.values())
# Print the last three elements (the three largest values) from the sorted list of values
print("the three largest values = ",dict[-3:])