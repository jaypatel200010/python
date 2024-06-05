import pymysql #import mysql after installing by "pip install pymysql"

mydb = pymysql.connect(host="localhost",user="root",password="") #by defaul for xampp
mycursor = mydb.cursor()

mycursor.execute("create database if not exists python50")  #SQL querry to create db if not exists
mydb.commit()  #To save

mydb = pymysql.connect(host="localhost",user="root",password="",database="python50") #to create table in db 
mycursor = mydb.cursor()

#creating table through sql query
mycursor.execute("create table if not exists python30 (id int primary key Auto_increment,name varchar(20),subject varchar(30))")
mydb.commit()