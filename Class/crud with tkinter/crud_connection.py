import pymysql
mydb = pymysql.connect(host="localhost",user="root",password="")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists college2_data")
mydb = pymysql.connect(host="localhost",user="root",password="",database="college2_data")
mycursor=mydb.cursor()
mycursor.execute("create table if not exists student(id int primary key auto_increment,name varchar(20),subject varchar(20))")
mydb.commit()