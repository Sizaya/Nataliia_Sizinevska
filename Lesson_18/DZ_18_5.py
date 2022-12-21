import mysql.connector

'''Creating a table "student"'''
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Qwerty12',
    database='my_first_db'
)

mycursor = mydb.cursor()
sql1 = "insert into student (primary_key, name) values (%s, %s)"
val1 = (1, 'John')
mycursor.execute(sql1, val1)
sql2 = "insert into employee (id, name, salary) values (%s, %s, %s)"
val2 = (1, 'John', 10000)
mycursor.execute(sql2, val2)
mydb.commit()