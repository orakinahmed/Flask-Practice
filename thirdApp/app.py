"""
DATA STRUCTURES
1. List - Arrays or a list of data | Implemented with a []
  Ex.    students = ["mary", "sue", "farz"]
         students[2]    #farz

2. Dictionary - Key - Value Pairs | Implemented with a {}
                Also known as Hash Tables in Java or JSON in APIs

   Ex.      person = {"name":"bob", "age":25, "ethnicity":"asain"}
            name = person['name']


Example of DIctionaries in Arrays
   people = [
                {"name":"bob", "age":25, "ethnicity":"asain"}, 
                {"name":"faraz", "age":56, "ethnicity":"white"}, 
                {"name":"rakin", "age":34, "ethnicity":"black"}
            ]

            name = people[2]["name"]

"""

from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"name":"bob", "age":25, "ethnicity":"asain"}, 
    {"name":"faraz", "age":56, "ethnicity":"white"}, 
    {"name":"rakin", "age":34, "ethnicity":"black"}
]

@app.route("/viewStudents", methods=['GET'])
def viewStudents():
    # DB.Connect()
    # DB.Table('Students')
    # students = DB.Query('Select * from Students')
    return jsonify(students)

@app.route("/addStudent", methods=["POST"])
def addStudent():
    newStudent = request.json
    print('Data from frontend:')
    print(newStudent)

    students.append(newStudent)
    return jsonify(students)

@app.route('/findStudentAgeByName', methods=["POST"])
def viewStudentAge():
    # Receive the data
    data = request.json #{'name':'faraz}
    name = data['name']

    print('The frontend data is:')
    print(name)
    age = ''

    for i in range(0, len(students)):
        currentStudent = students[i]

        if currentStudent['name'] == name:
            age = currentStudent['age']

    return jsonify({'age': age})

app.run(debug=True)

    