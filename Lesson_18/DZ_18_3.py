import mysql.connector

'''Creating a table "student"'''
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Qwerty12',
    database='my_first_db'
)

mycursor = mydb.cursor()
mycursor.execute("create table employee (id int auto_increment primary key, name varchar(255), salary int(6))")