#understandig flask restful api
from flask import Flask,request
from flask_restful import Resource,Api,reqparse

app=Flask(__name__)
api=Api(app)


items=[
    {
        'name':'Item1',
        'price':15.99
    },
    {
        'name':'Item2',
        'price':25.99
    },
    {
        'name':'Item3',
        'price':35.99
    }
]

class Item(Resource):
    #defining request parser
    parser=reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help='Price cannot be empty'
    )
    #get a particular item with its name
    def get(self,name):
        for item in items:
            if item['name']==name:
                return(item)
        return({
            'error':'Item not found'
        },404)

    #add a new item to existing items list
    def post(self,name):
        data=Item.parser.parse_args()
        items.append({
            'name':name,
            'price':data['price']
        })
        return 'item added successfully',201

    #delete an item from the items list
    def delete(self,name):
        for item in items:
            if item['name']==name:
                items.remove(item)
                return(items)
        return({
            'error':'item not present'
        },404)

    #modify existing item
    def put(self,name):
        for item in items:
            if item['name']==name:
                data=Item.parser.parse_args()
                item.update(data)
                return(items)
        return({
            'error':'item not present'
        },404)

class getAllItems(Resource):
    def get(self):
        return items


api.add_resource(Item,'/items/<string:name>')
api.add_resource(getAllItems,'/items/')

app.run(port=3000,debug=True)
