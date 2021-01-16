from flask import Flask, redirect, url_for, request, render_template, session
import sqlite3 as lit

app = Flask(__name__)


@app.route('/main')
def mainpage():
    return render_template("mainpage.html")


@app.route('/login', methods=['POST', 'GET'])
def login():

    r=""
    msg=" "
    if(request.method == "POST"):
        username = request.form['name']
        password = request.form['password']
        print(username + password)
        connection = lit.connect("userdata.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username= '"+username+"' and password ='"+password+"' ")
        r = cursor.fetchall()
        for i in r:
            if(username == i[0] and password == i[1]):
                return redirect(url_for('mainpage'))
        else:
            msg = "Please enter valid username and password"
    return render_template('login.html',msg=msg)




@app.route('/user/signup', methods=['POST'])
def signup():
    username = request.form['unm']
    password = request.form['psd']
    rname = request.form['nm']
    email = request.form['email']

    print(username + "" + password + "" + rname + "" + email)
    connection = lit.connect("userdata.db")
    cursor = connection.cursor()
    query1 = "INSERT INTO users VALUES('{un}','{pd}','{n}','{em}')".format(un=username, pd=password, n=rname, em=email)
    cursor.execute(query1)
    connection.commit()
    return render_template("login.html")


@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
