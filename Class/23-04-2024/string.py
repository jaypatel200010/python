s = "Tops Technologies"

print(len(s))   #return length
print(type(s))  #return type


print(s.capitalize()) #first letter capital
print(s.casefold()) #First letter small
print(s.lower()) #convert into lower case
print(s.upper()) #convert into upper case
print(s.center(30,"*"))  #center content using pattern
print(s.count("T")) #counts T
print(s.endswith("se")) #return true or false acc
print(s.find("T",2)) #finds after index given letter
print(s.index("o"),11) #finds index
print(s.isalnum()) #check for alpha num
print(s.replace("T","w")) #replace T with W
print(s.swapcase()) #small to capital and viveversa

S1 = '-'.join(s)
print(S1) #joins all letters with -

