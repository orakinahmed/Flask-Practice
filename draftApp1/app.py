"""
    1. Create a Flask App 
    2. Create a GET route & a POST route
    3. Return JSON data in routes
    4. Run your app
"""

"""
What is rest?
REST in an architecture to code apis to mimic HTTP web requests

What is an api?
an api is a interface that communicates and performs tasks between the server and client.

what are routes/endpoints?
Routes are a web location that can be navigated to with a specific 

what is a web framework?
a web framework is a collection of libraries/ modules used to create a website and its tools

how do you perform a get request?
a get request is a request given to the server by the client in order to retrieve data back from it.

how do you perform a post request?
a post request is a request that is used to save or update data within a server.

what does a wrapper do in a function?
a wrapper enhances or gives powers to a function | Symbol: @

"""
# Flask is a webframework, which contains libraries/modules, that is used to build websites 
# REST APIs -
# Retrieve Data - GET | Saves/Update Data - POST
# Request - Client (POSTMAN | UI) sents out Request to Server (Python API) to a specific Route/Endpoint
# Response - Server Responds with Data to the Client & a Status Code | 200 = Success | 4xx - Client Error | 5xx - Server Error


# import web framework for python
from flask import Flask, jsonify, render_template, request


# Create an instance of flask app, which has a variable that contains the powers of Flask
app = Flask(__name__)

# create some dictionaries in arrays
contacts = [
    {"name":"bob", "age":23, "ethnicity":"asian"}, 
    {"name":"faraz", "age":45, "ethnicity":"hispanic"}, 
    {"name":"rakin", "age":67, "ethnicity":"caucasian"}
]
#access value with: name = people[2]["name"]   


# create a wrapper function that allows navigation to the route
@app.route('/', methods=['GET'])
def mainPage():
    return render_template('index.html')        #use templates to render HTML which will display in the user's browser.

@app.route('/home')                             #defaulted to a GET route
def homePage():                                 #function that turns into a flask response
    return jsonify("Welcome!")                  #Flask functions HAVE to return json data or html

@app.route('/login', methods=['GET','POST'])    #must put POST route or GET/POST route
def loginPage():
    return jsonify({'username': 'Rakin05'})

app.route('/viewContacts', methods=["POST"])
def viewContacts():
    return jsonify(contacts)



# Create a POST Request /newContact that takes in a JSON with name, email, and phone
@app.route('/newContact', methods=['POST'])
def addContact():
    data = request.json                         #data from request (frontend) ----- Gets data from client
    print(data)                                 #prints data
    #code needed to save contact in DB:
    #contact the DB
    #save to DB
    return jsonify({'message': 'New contact added!'})

# run the flask app
app.run(debug=True, port=7111)

