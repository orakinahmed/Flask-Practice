"""
What is rest
REST in an architecture to code apis to mimic HTTP web requests

What is an api
an api is a interface that communicates and performs tasks between the server and client.

what are routes/endpoints
Routes are a web location that can be navigated to with a specific 

what is a web framework
a web framework is a collection of libraries/ modules used to create a website and its tools

how do you perform a get request
a get request is a request given to the server by the client in order to retrieve data back from it.

how do you perform a post request
a post request is a request that is used to save or update data within a server.

what does a wrapper do in a function
a wrapper enhances or gives powers to a function | Symbol: @

"""

# retrieving flask from flask
from flask import Flask, jsonify, request

# Create an instance of flask app
app = Flask(__name__)

# Define flask wrapper | Create flask function
@app.route('/home')
def homePage():
    return jsonify({'home': 'mainpage'})

# Create a POST Request /newContact that takes in a JSON with name, email, and phone
@app.route('/newContact', methods=['POST'])
def addContact():
    newContact = request.json   # Gets data from client
    print(newContact)           # print data

    return jsonify({'message': 'successful new contact!'})

# Make Flask App Run
app.run(debug=True) 

# Faraz testing