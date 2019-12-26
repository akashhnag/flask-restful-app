import sqlite3

connection=sqlite3.connect('users.db')
cursor=connection.cursor()

user_table='CREATE TABLE users(id INTEGER PRIMARY KEY,username text,password text)'
cursor.execute(user_table)

connection.close()
