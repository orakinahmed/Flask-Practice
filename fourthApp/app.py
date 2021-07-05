# importing web framework for python
from flask import Flask, jsonify

# Making a variable with the powers of Flask
app = Flask(__name__)

@app.route('/home')         # Creates a flask wrapper that allows navigation to the route
def homepage():             # A Python Function that turns into a Flask Response
    return jsonify({'username':'rakin'})

app.run()



