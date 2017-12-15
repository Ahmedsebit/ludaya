from flask import Flask, render_template, session, flash, request, redirect, url_for, flash
from flask.ext.sqlalchemy import SQLAlchemy
import os
import re
from flask import Blueprint, request, session, g, redirect, url_for, abort, \
     render_template, flash, current_app
from validate_email import validate_email
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User


@app.route('/')
def hello():
    return render_template('home.html')


@app.route('/register', methods=['POST'])
def register():
    is_valid = validate_email(request.form['email'])
    if is_valid:
        user = User.query.filter_by(email=request.form['email']).first()
        if not user:
            # try:
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            password = request.form['password']
            print(firstname)
            if email is None or password is None:
                response = {'message': 'Invalid input. Check the email and password'}
                error = 'Empty email or password'
                return redirect(url_for('hello_name'))
            else:
                user = User(firstname=firstname, lastname=lastname, email=email)
                user.hash_password(password)
                db.session.add(user)
                db.session.commit()
                response = {'message': 'Invalid input. Check the email and password'}
                flash('You were successfully register')
                return redirect(url_for('hello'))
        else:
            response = {'message': 'User already exists. Please login.'}
            error = 'User already exists'
            return render_template('signup.html')
    else:
        response = {'message': 'hello_name'}
        error = 'Invalid email'
        return render_template('signup.html')