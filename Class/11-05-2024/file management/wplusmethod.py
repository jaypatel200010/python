file = open("C:\\Users\\ASUS\\Desktop\\Tops\\python\\Class\\11-05-2024\\file management\\test3.txt","w+")
file.write("Hello my name is jay")

print(file.tell()) #show the position of cursor
file.seek(0) #sends the cursor to the position given
print(file.readline())
file.close()