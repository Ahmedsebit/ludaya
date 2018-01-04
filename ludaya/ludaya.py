from flask import Flask, render_template, session, flash, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
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
def home():
    return render_template('home.html')


@app.route('/register', methods=['POST'])
def register():
    is_valid = validate_email(request.form['email'])
    error = None
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
                error = 'Empty email or password'
            else:
                user = User(firstname=firstname, lastname=lastname, email=email)
                user.hash_password(password)
                db.session.add(user)
                db.session.commit()
                response = {'message': 'Invalid input. Check the email and password'}
                flash('You were successfully register')
                return redirect(url_for('home'))
        else:
            error = 'User already exists'
    else:
        error = 'Invalid email'
    return render_template('home.html', error=error)


@app.route('/login', methods=['POST'])
def login():
    '''
    Function for login user
    '''
    try:
        user = User.query.filter_by(email=request.form['email']).first()
        if user and user.verify_password(request.form['password']):
            session['username'] = request.form['email']
            session['id'] = user.id
            return redirect(url_for('issues'))
        else:
            error = 'Invalid email or password, Please try again.'
            return render_template('home.html', error=error)
    except:
        error = 'No email or password field!!'
        return render_template('home.html', error=error)


@app.route('/issues')
def issues():
    if 'username' in session:
        username = session['username']
        id = session['id']
        # items = sessions.query(Issues).filter_by(user_id=id)
        return render_template('index.html', items='items')
    else:
        return redirect(url_for('home'))


@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('home'))