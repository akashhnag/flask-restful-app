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
        connection=sqlite3.connect('users.db')
        cursor=connection.cursor()

        user='SELECT * FROM users'
        result=[]
        for row in cursor.execute(user):
            result.append(row)
        return result

        connection.close()

    def add_user(data):
        print('adding user in db',data)
        connection=sqlite3.connect('users.db')
        cursor=connection.cursor()

        show_user='SELECT * FROM users WHERE username=?'
        execute_query=cursor.execute(show_user,(data['username'],))
        result=execute_query.fetchone()
        if result:
            print(result)
            return result
        else:
            print('no result')
            insert_user='INSERT INTO users VALUES(NULL,?,?)'
            cursor.execute(insert_user,(data['username'],data['password'],))
            return 'done'

        connection.commit()
        connection.close()

    def authenticate(data):
        print('add users',data)
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        username=data['username']
        password=data['password']
        user='SELECT * FROM users WHERE username=? AND password=?'
        value=cursor.execute(user,(username,password,))
        result=value.fetchone()
        return result
        connection.close()
