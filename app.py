print("Hello world!")

# # Store this code in 'app.py' file


import email
from sqlite3 import Time
from telnetlib import NOP
from time import time
from flask import Flask , render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re


app = Flask(__name__,template_folder="templates")
app.secret_key = "super secret key"


app.config['MYSQL_HOST'] = 'us-cdbr-east-06.cleardb.net'
app.config['MYSQL_USER'] = 'ba63390635159b'
app.config['MYSQL_PASSWORD'] = '8f6e310e'
app.config['MYSQL_DB'] = 'heroku_96a5a3444f06fe0'

mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('mainindex.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    value=''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM signup_driver WHERE Email = % s AND Password = % s', (email, password))
        account = cursor.fetchone()
        print(account)
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['email'] = account['email']
            msg = 'Logged in successfully !'
            if account['Type'] == 'driver':
                value=account['idsignup_driver']
                value=int(value)

                return render_template('post_ride.html', msg=msg,value=value)
            if account['Type'] == 'passenger':
                value=account['idsignup_driver']
                value=int(value)
                cursor = mysql.connection.cursor()
                cursor.execute("""SELECT * FROM rides WHERE Seat_Available > 0; """)
                data=cursor.fetchall()
                print(data)
                return render_template('rides.html', data=data,msg=msg,value=value)
        else:
            msg = 'Incorrect username / password !'
    return render_template('mainindex.html', msg=msg)


@app.route('/logout')
def logout():
    return render_template('mainindex.html')
#     session.pop('loggedin', None)
#     session.pop('id', None)
#     session.pop('username', None)
#     return redirect(url_for('login'))


@app.route('/post_ride', methods=['GET', 'POST'])
def register():
    return render_template('mainindex.html')
#     msg = ''
#     value=''
#     if request.method == 'POST' and 'email' in request.form and 'password' in request.form and 'confirmpassword' in request.form and 'fullname' in request.form and 'cmp' in request.form and 'in' in request.form and 'dl' in request.form and 'age' in request.form and 'pn' in request.form and 'gender' in request.form:
#         email = request.form['email']
#         password = request.form['password']
#         confirmpassword = request.form['confirmpassword']
#         name = request.form['fullname']
#         cmp = request.form['cmp']
#         inumber = request.form['in']
#         dl = request.form['dl']
#         Age = request.form['age']
#         pn = request.form['pn']
#         Gender = request.form['gender']
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute(
#             'SELECT * FROM signup_driver WHERE Email = % s', (email, ))
#         account = cursor.fetchone()
#         if account:
#             msg = 'Account already exists !'
#         elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
#             msg = 'Invalid email address !'
#         elif not re.match(r'[A-Za-z0-9]+', inumber):
#             msg = 'Insurance number must contain only characters and numbers !'
#         elif not re.match(r'[0-9]+', dl):
#             msg = 'Driving Licence Number  must contain only numbers !'
#         elif not re.match(r'[0-9]+', Age):
#             msg = 'Age  must contain only numbers !'
#         elif not re.match(r'[0-9]+', pn):
#             msg = 'pn  must contain only numbers !'
#         elif not re.match(r'[A-Za-z]+', Gender):
#             msg = 'Gender  must contain only characters !'
#         elif not Gender or not pn or not Age or not cmp or not inumber or not dl or not confirmpassword or not name or not password or not email:
#             msg = 'Please fill out the form !'
#         else:
#             cursor.execute('INSERT INTO signup_driver VALUES (NULL, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s)',
#                            (name, email, password, inumber, dl, cmp, Age, Gender, pn, 'driver'))
#             mysql.connection.commit()
#             msg = 'You have successfully registered !'
#             cursor.execute(
#             'SELECT * FROM signup_driver WHERE Email = % s', (email, ))
#             account = cursor.fetchone()
#             if account:
#                 value=account['idsignup_driver']
#                 value=int(value)

#     elif request.method == 'POST':
#         msg = 'Please fill out the form !'
#     return render_template('post_ride.html', msg=msg,value=value)


@app.route('/rides', methods=['GET', 'POST'])
def registernew():
    return render_template('mainindex.html')
#     isSelected = -1
#     def selectMethod(index):
#         isSelected =index
#     msg = ''
#     if request.method == 'POST' and 'email' in request.form and 'password' in request.form and 'confirmpassword' in request.form and 'fullname' in request.form and 'age' in request.form and 'pn' in request.form and 'gender' in request.form:
#         email = request.form['email']
#         password = request.form['password']
#         confirmpassword = request.form['confirmpassword']
#         name = request.form['fullname']
#         Age = request.form['age']
#         pn = request.form['pn']
#         Gender = request.form['gender']
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute(
#             'SELECT * FROM signup_driver WHERE Email = % s', (email, ))
#         account = cursor.fetchone()
#         if account:
#             msg = 'Account already exists !'
#         elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
#             msg = 'Invalid email address !'

#         elif not re.match(r'[0-9]+', Age):
#             msg = 'Age  must contain only numbers !'
#         elif not re.match(r'[0-9]+', pn):
#             msg = 'pn  must contain only numbers !'
#         elif not re.match(r'[A-Za-z]+', Gender):
#             msg = 'Gender  must contain only characters !'
#         elif not Gender or not pn or not Age or not confirmpassword or not name or not password or not email:
#             msg = 'Please fill out the form !'
#         else:
#             cursor.execute('INSERT INTO signup_driver VALUES (NULL, % s, % s, % s, NULL, NULL, NULL, % s, % s, % s, % s)',
#                            (name, email, password, Age, Gender, pn, 'passenger'))
#             mysql.connection.commit()
#             cursor = mysql.connection.cursor()
#             cursor.execute("""SELECT * FROM rides WHERE Seat_Available > 0; """)
#             data=cursor.fetchall()
#             print(data)
#             msg = 'You have successfully registered !'
#     elif request.method == 'POST':
#         msg = 'Please fill out the form !'
#     print(msg)
#     return render_template('rides.html', data=data,msg=msg,selectMethod = selectMethod)



@app.route('/registernew1', methods=['GET', 'POST'])
def registernew1():
    return render_template('mainindex.html')
#     msg = ''
#     print('I am inside this fucntion')
#     if request.method == 'POST' and 'origin' in request.form and 'destination' in request.form and 'date' in request.form and 'nops' in request.form and 't' in request.form:
#         print('I am storing the values ')
#         origin = request.form['origin']
#         destination = request.form['destination']
#         print(destination)
#         d = request.form['date']
#         nops = request.form['nops']
#         t = request.form['t']
#         id= request.form['driverid']
#         print(id)
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

#         if not re.match(r'[A-Za-z0-9]+', origin):
#             msg = 'Origin  must contain an address !'
#         elif not re.match(r'[A-Za-z0-9]+', destination):
#             msg = 'destination must contain an address !'
#         elif not re.match(r'[0-9-/]+', d):
#             msg = 'Date should cotain  - or / !'
#         elif not re.match(r'[0-9 :]+', t):
#             msg = 'Time must conatain : !'
#         elif not re.match(r'[0-9]+', nops):
#             msg = 'No of passangers must be in munbers only  !'

#         elif not origin or not destination or not d or not nops or not t:
#             msg = 'Please fill out the form !'
#         else:
#             cursor.execute('INSERT INTO rides VALUES ( % s, % s, % s, % s, % s,NULL, % s,NULL)',
#                            (nops, origin, destination, t, d, id))
#             mysql.connection.commit()
#             msg = 'You have successfully posted a ride !'
#     elif request.method == 'POST':
#         msg = 'Please fill out the form !'
#     cursor.execute(' select idrides FROM rides WHERE driver_id = % s ',(id,))
        
#     value=cursor.fetchall()
#     print(value)
#     rides = {}
#     finaloutput={}
#     for i in value:
#         print(i['idrides'])
#         count=i['idrides']
#         cursor.execute('select pass_id FROM details WHERE ride_id = % s ',(i['idrides'],))
#         passid_details=cursor.fetchall()
#         rides.update({count:passid_details}) 
#         finaloutput.update({count:''})
#         print(rides)
#         for j in passid_details:
#             print("Inside the Loop")
#             print(j)
#             cursor.execute('select FULLL_Name,pnumber FROM signup_driver WHERE idsignup_driver = % s ',(j['pass_id'],))
#             x=j['pass_id']
#             #for key,val in finaloutput:
#                 #print("The Key is ",key)
#                 #if count==key :
#             finaloutput[count] = [finaloutput[count],{x:cursor.fetchall()}]
#                 #else:
#                     #finaloutput.update({x:cursor.fetchall()})
#             print("Updated List is ",finaloutput)
    
#     print(finaloutput)
#     print("Printing each item")
#     return render_template('driver_details.html', msg=msg, value=finaloutput)



@app.route('/passenger_ride_details.html',methods=['GET', 'POST'])
def passenger_ride_details():
    return render_template('mainindex.html')
#     value=request.form['check']
#     passid=request.form['passid']
#     driver_acc=''
#     print(value)
#     print(passid)
#     #value=int(value)
#     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     cursor.execute(
#         'SELECT * FROM rides WHERE idrides = % s ', (value,))
#     account = cursor.fetchone()
#     print('Fetched account')
#     rideid=account['idrides']
#     Seat=int (account['Seat_Available'])
#     print(account)
#     if account:
#         driver_id=account['driver_id']
#         #print(driver_id)
#         cursor.execute(
#         'SELECT Fulll_Name , Car_Number_Plate FROM signup_driver WHERE idsignup_driver = % s ', (driver_id,))
#         driver_acc=cursor.fetchone()
#         print(driver_acc)
#         #print('Trying to merge two tuples')
#         account.update(driver_acc)
#         #print(account)
#         cursor.execute('SELECT * From signup_driver WHERE idsignup_driver = % s',(passid,))
#         pass_account=cursor.fetchone()
#         print(pass_account)
#         cursor.execute('INSERT INTO details VALUES ( NULL, % s, % s)',(passid,rideid,))

#         mysql.connection.commit()
#         #cursor.execute('select Seat_Available FROM rides WHERE idrides = rideid')
#         #Seat=cursor.fetchone()
#         print(Seat)
#         cursor.execute('UPDATE rides SET Seat_Available = % s WHERE idrides = % s',((Seat - 1),rideid,))
#         mysql.connection.commit()


#     return render_template('passenger_ride_details.html',details=account)




if __name__ == '__main__':
    app.run()
