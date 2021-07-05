from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/newLogin', methods=["POST"])
def newLogin():
    data = request.json()                   #incoming data from request body     {'username':'faraz', 'password': '12345'}
    username = data["username"]
    password = data['password']

    # Save to DB

    if username == 'faraz':
        return jsonify({'message':'hes a bitch'})       #outgoing data
    else:
        return jsonify({'message':'hes a hoe'})         #outgoing data


# Ex. 127.0.0.1:5000/getAddressByName?name=Faraz
@app.route('/getAddressByName')
def getAddressByName():
    #addresses = {"rakin": "123 chicken lne", "faraz":'455 butt lane'}
    data = request.args.get('name')         #incoming data from GET url arguments

    addresses = [
        {'name':'Rakin', 'address': '123 Chicken Ln'},
        {'name': "Faraz", 'address': '321 Bunny Rd'},
        {'name': 'Jack', 'address': '456 Rat Way'}          
    ]

    for index in range(0, len(addresses)):
        address = addresses[index]["address"]
        if data == addresses[index]['name']:
            return jsonify({"address": address})


app.run()

# Tools of a programmer
"""
1. For Loop - to repeat tasks or go through a list of items
2. If Statement - to check for things
3. Functions - to do a small task
4. Dictionary - to describe some data
5. List - to have a list of items
6. Set- to have unique values
"""