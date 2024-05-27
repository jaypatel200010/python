# 35] How Do You Traverse Through A Dictionary Object In Python?
# Define a dictionary named dict1 with key-value pairs
dict1 = {'jay': 1, 'tushar': 2, 'himanshu': 3, 'raj': 4, 'nikhil': 5, 'ketan': 6}
# Iterate over key-value pairs in the dictionary using the items() method
for i, j in dict1.items():
    # Print each key-value pair using formatted string
    print(f'{i} : {j}')
# The loop iterates through all key-value pairs in the dictionary, printing each pair