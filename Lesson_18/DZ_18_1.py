import mysql.connector

'''Creating a Database'''
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Qwerty12'
)

mycursor = mydb.cursor()
mycursor.execute("create database my_first_db")