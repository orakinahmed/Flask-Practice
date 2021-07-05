from flask import Flask, jsonify

# Created new flask app
app = Flask(__name__)

@app.route('/rakin')
def home():
    return "Hello There!"

app.run(debug=True)



