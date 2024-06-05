from tkinter import *

def login():
    root = Tk() #init

    root.geometry("500x500")
    root.title("Login Form!!")

    email = Label(root,text="Email",font=("caliberi",12,"bold"))
    email.place(x=50,y=50)

    password = Label(root,text="Password",font=("caliberi",12,"bold"))
    password.place(x=50,y=100)


    eemail = Entry(root,bg="yellow")
    eemail.place(x=160,y=50)

    epassword = Entry(root,bg="yellow")
    epassword.place(x=160,y=100)


    login1 = Button(root,font=("arial",18,"italic"),fg="red",text="Login")
    login1.place(x=150,y=150)



    root.mainloop()