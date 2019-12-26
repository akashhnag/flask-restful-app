from flask import Flask,jsonify
from flask_restful import Resource,Api,reqparse
from user import User

app=Flask(__name__)
api=Api(app)

class Users(Resource):
    def get(self,name):
        print(name)
        user=User.get_user_by_username(name)
        print('get user',user)
        if user:
            return jsonify(user)
        else:
            return({
                'error':'User not present'
            },404)

class GetAllUsers(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help='username cannot be empty'
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help='password cannot be empty'
    )

    def get(self):
        print('get all')
        users=User.get_all_users()
        return users

    def post(self):
        data=GetAllUsers.parser.parse_args()
        result=User.add_user(data)
        if result=='done':
            return({'message':'User registered'},201)
        else:
            return({'error':'User already present'})

class Authenticate(Resource):
    def post(self):
        data=GetAllUsers.parser.parse_args()
        result=User.authenticate(data)
        if result:
            print(result)
            return(jsonify(result))
        else:
            print('User not present')
            return({'error':'Username or password incorrect'},404)

api.add_resource(Users,'/users/<string:name>')
api.add_resource(GetAllUsers,'/users')
api.add_resource(Authenticate,'/authenticate')


app.run(port=3000,debug=True)
