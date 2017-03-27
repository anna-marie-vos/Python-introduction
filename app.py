#!/usr/bin/env python3

from flask import Flask, render_template, request, json
# from flask-mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash


app = Flask(__name__)
# mysql = MySQL()
# # MySQL configurations
# # dotenv not working yet
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'Icu@mysql01!'
# app.config['MYSQL_DATABASE_DB'] = 'BucketList'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)
#
# conn = mysql.connect()
# cursor = conn.cursor()

#Basic route
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp', methods=['POST'])
def signUp():
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    if _name and _email and _password:
        return json.dumps({'html': '<span>All fields good!!</span>'})
    else:
        return json.dumps({'html': '<span>Enter the required fields.</span>'})

if __name__ == "__main__":
    app.run()
