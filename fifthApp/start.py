# Flask is a webframework that is used to build websites | Contains libraries/modules to do so
from flask import Flask, jsonify, render_template, request

# Defines our flask app
app = Flask(__name__)


#REST APIs
# Retrieve Data - GET | Saves/Update Data - POST
# Request - Client (POSTMAN | UI) sents out Request to Server (Python API) to a specific Route/Endpoint
# Response - Server Responds with Data to the Client & a Status Code | 200 = Success | 4xx - Client Error | 5xx - Server Error

# @ is a wrapper in python that enhances a function with some ability in this case navigation
@app.route('/', methods=['GET'])     
def home():
    # Flask functions HAVE to return json data or html
    return render_template('index.html')

@app.route('/newContact', methods=['POST'])
def newContact():
    data = request.json # data from request (frontend)
    print(data)

    # db = ConnectToDB()
    # db.save(data)

    return jsonify({'message':'SUCCESSFULLY ADDED NEW CONTACT!'})

# Runs our flask app
app.run(debug=True, port=7111)
