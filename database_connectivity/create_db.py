import sqlite3

connection=sqlite3.connect('data.db')
cursor=connection.cursor()

create_table='CREATE TABLE users(id int,username text,password text)'
cursor.execute(create_table)

insert_user='INSERT INTO users VALUES(?,?,?)'
user=(1,'akash','fdsf')
cursor.execute(insert_user,user)

users=[
    (2,'ramesh','fdafe'),
    (3,'amar','ffesv')
]
cursor.executemany(insert_user,users)

show='SELECT * FROM users'
for row in cursor.execute(show):
    print(row)

#add commit when adding or making changes to exiting values in a database
connection.commit()
connection.close()
