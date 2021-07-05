"""
    1. Create a Flask App
    2. Create a GET route & a POST route
    3. Return JSON data in routes
    4. Run your app

    Ex. {   
            'username': 'Bob99', 
            'color': 'red'
        }
"""
from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/home')
def mainpage():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def loginpage():
    return {'username': 'Bob99'}

app.run()
