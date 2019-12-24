from flask import Flask,jsonify,request

app=Flask(__name__)

stores=[
    {
        'name':'my_store',
        'items':[
            {
                'name':'Item 1',
                'price':15.99
            }
        ]
    }
]

#get stores
@app.route('/store')
def getStore():
    print('get store')
    return jsonify({'stores':stores})

#get particular store
@app.route('/store/<string:name>')
def getStoreName(name):
    print('store name is',name)
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return {'error':'store not found'}

#create a store
@app.route('/store/',methods=['POST'])
def createStore():
    #request_data=request.get_json()
    print('create store',request.get_json())
    stores.append(request.get_json())
    return jsonify(stores)

#get items from store
@app.route('/store/<string:name>/item')
def getStoreItem(name):
    print('getting store item..',name)
    for store in stores:
        if store['name']==name:
            return jsonify(store['items'])
    return({'error':'store not present'})

#add items to store
@app.route('/store/<string:name>/item',methods=['POST'])
def createStoreItem(name):
    print('creating store item..',request.get_json())
    for store in stores:
        if store['name']==name:
            store['items'].append(request.get_json())
            return jsonify(store)
    return ({'error':'store not found'})


app.run(port=4000)
