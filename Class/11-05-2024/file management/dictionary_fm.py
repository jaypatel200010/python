import random
# file = open("C:\\Users\\ASUS\\Desktop\\Tops\\python\\Class\\11-05-2024\\file management\\test2.txt","w")

d = {}
l1 = random.randint(1001,9999)
while True:
    menu = """
    press 1 for sign-up.
    press 2 for login.
    press 3 for forgotpass.
    press 3 for exit.
    
""" 
    print(menu)

    choice = int(input("Enter choice : "))

    if choice == 1:
        print ("Sign-up here..!")

        name = input("enter name : ")
        email = input("enter email : ")
        mobile = int(input("enter mobile : "))
        password = input("enter password : ")
        confirm_password = input("confirm password : ")

        # d["name"] = name
        # d["email"] = email
        # d["password"] = password
        # d["mobile"] = mobile

        
        # file.write("name")
        # file.write("email")
        # file.write("password")
        # file.write("mobile")

        file = open("C:\\Users\\ASUS\\Desktop\\Tops\\python\\Class\\11-05-2024\\file management\\test2.txt","w")

        d["login"] = {'name' : name, 'email' : email, 'mobile' : mobile, 'password' : password}

        d1 = str(d)
        file.write(d1)
        file.close()
        
        if password==confirm_password:
            print ("sign up success : ")
        else:
            print("pass and confirm pass did not match!!!!")

    elif choice == 2:
        print ("Login here!!!!")
        email = input("enter email : ")
        password = input("enter pass : ")
        if d["email"] == email and d["password"] == password:
            print("Login success : ")
        else:
            print("Invalid credentials : ")

    elif choice == 3:
        mobile = int(input("enter mobile : "))
        if d["mobile"] == mobile:
            print(l1)
            otp = int(input("enter otp : "))
            if otp == l1:
                print("pass changed success")
            else:
                print("invalid otp")
        else:
            print("invalid mobile")

    elif choice == 4:
        print("Thanks")
        break
    else:
        print("invalid choice!!!")
        break
        