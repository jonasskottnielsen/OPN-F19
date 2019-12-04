import mysql.connector  
from mysql.connector import Error
from flask import Flask, request, json

backend = Flask(__name__)

def connect():
    connection = mysql.connector.connect(host='db_container',
                                         database='aperson',
                                         user='root',
                                         password='')
    return connection
                                        

@backend.route('/person', methods = ['POST'] )
def person():
    connection = connect()
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    mySQL_insert = "INSERT INTO Persontable (fname, lname) VALUES ('%s', '%s');" % (firstname, lastname)
    cursor = connection.cursor()
    cursor.execute(mySQL_insert)
    connection.commit()
    return "succes"

@backend.route('/persons', methods = ['GET'] )
def persons():
        connection = connect()
        sql_select_Query = "select * from Persontable;"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        personlist = []
        person = {}   
        for row in records:
            person = {
            "PersonID": row[1],
            "Firstname": row[0], 
            "Lastname": row[2]}

            personlist.append(person)
        return json.dumps(personlist)

if __name__ == '__main__':
    backend.run(host='0.0.0.0')

