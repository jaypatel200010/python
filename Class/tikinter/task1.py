from tkinter import *
from task2 import *

root = Tk() #init

root.geometry("500x500")
root.title("Signup Form!!")

id = Label(root,text="Id",font=("caliberi",12,"bold"))
id.place(x=50,y=50)

name = Label(root,text="Name",font=("caliberi",12,"bold"))
name.place(x=50,y=100)


email = Label(root,text="Email",font=("caliberi",12,"bold"))
email.place(x=50,y=150)

mobile = Label(root,text="Mobile",font=("caliberi",12,"bold"))
mobile.place(x=50,y=200)

password = Label(root,text="Password",font=("caliberi",12,"bold"))
password.place(x=50,y=250)

eid = Entry(root,bg="yellow")
eid.place(x=180,y=50)


ename = Entry(root,bg="yellow")
ename.place(x=180,y=100)

eemail = Entry(root,bg="yellow")
eemail.place(x=180,y=150)

emobile = Entry(root,bg="yellow")
emobile.place(x=180,y=200)

epassword = Entry(root,bg="yellow")
epassword.place(x=180,y=250)

insert = Button(root,font=("arial",18,"italic"),fg="red",text="Insert")
insert.place(x=50,y=300)

update = Button(root,font=("arial",18,"italic"),fg="red",text="Update")
update.place(x=150,y=300)

delete = Button(root,font=("arial",18,"italic"),fg="red",text="Delete")
delete.place(x=280,y=300)


login = Button(root,font=("arial",18,"italic"),fg="red",text="Login",command=login)
login.place(x=400,y=300)

root.mainloop()