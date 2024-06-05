from connection import * #imported everything from connection

mydb = pymysql.connect(host="localhost",user="root",password="",database="python50")
mycursor = mydb.cursor()

while True:
    menu = """

    press 1 for insert data
    press 2 for read data
    press 3 for update data
    press 4 for delete data
    press 5 for exit

"""

    print(menu)
    choice = int(input("Enter Choice : "))

    # For inserting data 
    if choice==1:
        name = input("Enter Name : ")
        subject = input("Enter Subject : ")

        #Query to insert data into table
        query = "insert into python30(name,subject) values ('%s','%s')"
        args = (name,subject)
        mycursor.execute(query % args) # % to execute query and args 
        mydb.commit() #to save
        print("Data Inserted!!")

    # to fetch data (Read)
    elif choice==2:
        #Query to select all data from db
        query = "select * from python30"
        mycursor.execute(query) #execute query
        #Fetching all data using fetchall()
        data = mycursor.fetchall()
        print(data)

    # to update data 
    elif choice==3:
        #taking data to be updated
        id = int(input("Enter Id : "))
        name = input("Enter Name : ")
        subject = input("Enter Subject : ")

        #query to update the data
        query = "update python30 set name='%s',subject='%s' where id='%s'"
        args  = (name,subject,id)

        mycursor.execute(query % args) #Execute query and args
        mydb.commit() #save
        print("Data Updated!!")

    # to delete data from db
    elif choice==4:
        #id in which data is to be deleted
        id = int(input("Enter Id : "))
        #Query to delete data from db
        query = "delete from python30 where id='%s'"
        args = (id)
        mycursor.execute(query % args)
        mydb.commit()
        print("Data Deleted!!")

    elif choice==5:
        print("Thank you!!")
        break

    else:
        print("Invalid Choice!!")
        break