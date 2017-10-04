
from flask import Flask
from flask_mysqldb import MySQL
mysql = MySQL()
app = Flask(__name__)
# My SQL Instance configurations 
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'studentbook'
app.config['MYSQL_HOST'] = '35.197.216.20'
mysql.init_app(app)

# The first route to access the webservice fromhttp://external-ip:5000/ 
#@pp.route("/add") this will create a new endpoints that can be accessed usinghttp://external-ip:5000/add
@app.route("/")
def hello(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM students''') # execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    return str(rv)      #Return the data in a string format

#a part
@app.route("/addRecord")
def addRecord():
	cur = mysql.connection.cursor()
	cur.execute('''INSERT INTO students (studentName, email) values("Daragh", "daragh@mydit.ie")''')
	cur.execute('''SELECT * FROM students''')
	rv = cur.fetchall()
	return str(rv)
#b part
@app.route("/updateRecord")
def updateRecord():
        cur = mysql.connection.cursor()
        cur.execute('''UPDATE students SET email='newemail@mydit.ie' WHERE studentID = 1''')
        cur.execute('''SELECT * FROM students''')
        rv = cur.fetchall()
        return str(rv)
#c part
@app.route("/deleteRecord")
def deleteRecord():
        cur = mysql.connection.cursor()
        cur.execute('''DELETE from students where studentID = 2''')
        cur.execute('''SELECT * FROM students''')
        rv = cur.fetchall()
        return str(rv)
#d part

if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000') #Run the flask app at port 5000
