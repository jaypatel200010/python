# 6] Write a Python program to read a file line by line and store it into a list.
# Open the file named "Q4.txt" in read mode
f1 = open("Q4.txt", "r")
# Print the list of lines
print("store in to list = ",f1.readlines())
# Close the file to free up system resources
f1.close()