# collections

# list:
# list is a collection data type in python we can store multiple data in single var

# represented by []
# list is mutable
# list allow duplicate values

l = [1,"jay",2,1.2356,"ketan",202]

print(type(l))
l.append(20)      #adds element at last 
print(l)

l.pop()           #removes element from last
print(l)

l.extend([20,"jp","hello"])     #adds whole list at last
print(l)

l.insert(2,200)             #insert element at particular index
print(l)

print(l.count(1))           #counts number

