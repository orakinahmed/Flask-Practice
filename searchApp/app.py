from flask import Flask, jsonify, request

app = Flask(__name__)

# 5 Contacts -> Name | State | Zip | Phone
contacts = [
    {'Name': 'Rakin', 'State': 'Georgia', 'Zip': 30021, 'Phone':'5201451100'},
    {'Name': 'Faraz', 'State': 'Florida', 'Zip': 56412, 'Phone':'456123321'},
    {'Name': 'Ben', 'State': 'Alaska', 'Zip': 98765, 'Phone':'65432112'},
    {'Name': 'Kevin', 'State': 'New York', 'Zip': 65432, 'Phone':'54165816'},
    {'Name': 'Jose', 'State': 'California', 'Zip': 12345, 'Phone':'541541651'}
]

# Return all contacts
@app.route('/getAllContacts')
def getAllContacts():
    return jsonify(contacts)

# Return contact info
@app.route('/getContactByName')
def getContactByName():
    contactName = request.args.get('name')

    for i in range(0, len(contacts)):
        currentName = contacts[i]['Name'] 
        if currentName == contactName:
            return jsonify(contacts[i])

# Return a json message with success
@app.route('/saveContact', methods=['POST'])
def saveContact():
    contactDetails = request.json
    contacts.append(contactDetails)

app.run(debug=True)
