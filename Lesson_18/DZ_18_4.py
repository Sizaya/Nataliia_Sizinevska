import mysql.connector

'''Creating a table "student"'''
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Qwerty12',
    database='my_first_db'
)

mycursor = mydb.cursor()
mycursor.execute("alter table student change id primary_key varchar(255)")