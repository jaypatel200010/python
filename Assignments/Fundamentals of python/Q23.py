# Write a Python function to insert a string in the middle of a string


def middle():
    # input for main string
  
    mainstring = input("Enter the main string : ")
    # enter the string to insert
   
    insertstring = input("Enter the string to insert : ")
    
    # Calculate the middle index of the main string
   
    middleindex = len(mainstring) // 2
    
    # Insert the insert string at the middle index of the main string
    
    result = mainstring[:middleindex] + insertstring + mainstring[middleindex:]
    
    # Return the modified string
    return result

# Example usage:
# Call the function to insert a string in the middle of another string
result = middle()

# Print the result

print("Result:", result)