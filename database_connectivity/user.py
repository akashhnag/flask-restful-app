import sqlite3
class User():
    def __init__(self,_id,username,password):
        self._id=_id
        self.username=username
        self.password=password

    def get_user_by_username(username):
        print('fetch by username',username)
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        user='SELECT * FROM users WHERE username=?'
        result=cursor.execute(user,(username,))
        user=result.fetchone()
        return user

        connection.close()

    def get_all_users():
        print('get all users')
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        user='SELECT * FROM users'
        result=[]
        for row in cursor.execute(user):
            result.append(row)
        return result

        connection.close()

    def add_users():
        print('add users')
        # connection=sqlite3.connect('data.db')
        # cursor=connection.cursor()

        # user='SELECT * FROM users'
        # result=[]
        # for row in cursor.execute(user):
        #     result.append(row)
        # return result

        # connection.close()
