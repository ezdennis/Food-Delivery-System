from flask import Flask, redirect, url_for, request, render_template, flash
import sqlite3 as lit

app = Flask(__name__)


@app.route('/main')
def mainpage():
    return render_template("mainpage.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    user = request.form['name']
    password = request.form['password']
    print(user + password)
    print("Hello world")

    if user == "admin" and password == "admin":
        return redirect(url_for('mainpage'))
    else:
        return render_template("login.html")


@app.route('/user/signup', methods=['POST'])
def signup():
    runame = request.form['unm']
    rpassword = request.form['psd']
    rname = request.form['nm']
    email = request.form['email']

    print(runame + "" + rpassword + "" + rname + "" + email)
    connection = lit.connect("userdata.db")
    cursor = connection.cursor()
    query1 = "INSERT INTO users VALUES('{un}','{pd}','{n}','{em}')".format(un=runame, pd=rpassword, n=rname, em=email)
    cursor.execute(query1)
    connection.commit()
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)
