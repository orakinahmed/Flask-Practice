from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'home': 'mainpage'})

@app.route('/', methods=['POST'])
def newContact():
    data = request.json
    print(data)

    # contact to db
    # save to db
    return jsonify({'message': 'success'})

app.run(debug=True)

