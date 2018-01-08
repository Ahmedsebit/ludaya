from flask import Flask, render_template, session, flash, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
import re
from flask import Blueprint, request, session, g, redirect, url_for, abort, \
     render_template, flash, current_app
from validate_email import validate_email
from flask_bootstrap import Bootstrap

from tasks.alltasks import communcation_list_length, electronics_list_length, hardware_list_length, learning_list_length, mac_list_length, maintainance_list_length, networking_list_length, security_list_length, server_list_length, support_list_length, unix_list_length, windows_list_length

app = Flask(__name__)
Bootstrap(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User, AssignedTask


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
        items = AssignedTask.query.filter_by(user_id=id).all()
        groups_list = []
        for i in items:
            groups_list.append(i.category)
        groups = {x:groups_list.count(x) for x in groups_list}

        all_communcation = communcation_list_length()
        all_electronics = electronics_list_length()
        all_hardware = hardware_list_length()
        all_learning = learning_list_length()
        all_mac = communcation_list_length()
        all_maintainance = maintainance_list_length()
        all_networking = networking_list_length()
        all_security = security_list_length()
        all_server = server_list_length()
        all_support = support_list_length()
        all_unix = unix_list_length()
        all_windows = windows_list_length()

        my_communication = [x for x in items if x.category == 'communication']
        my_electronics = [x for x in items if x.category == 'electronics']
        my_hardware = [x for x in items if x.category == 'hardware']
        my_learning = [x for x in items if x.category == 'learning']
        my_mac = [x for x in items if x.category == 'communication']
        my_maintainance = [x for x in items if x.category == 'maintainance']
        my_networking = [x for x in items if x.category == 'networking']
        my_security = [x for x in items if x.category == 'security']
        my_server = [x for x in items if x.category == 'server']
        my_support = [x for x in items if x.category == 'support']
        my_unix = [x for x in items if x.category == 'unix']
        my_windows = [x for x in items if x.category == 'windows']

        return render_template('index.html',
                               items=items,
                               groups=groups,
                               my_communication = len([x for x in items if x.category == 'communication']),
                               my_electronics = len([x for x in items if x.category == 'electronics']),
                               my_hardware = len([x for x in items if x.category == 'hardware']),
                               my_learning = len([x for x in items if x.category == 'learning']),
                               my_mac = len([x for x in items if x.category == 'communication']),
                               my_maintainance = len([x for x in items if x.category == 'maintainance']),
                               my_networking = len([x for x in items if x.category == 'networking']),
                               my_security = len([x for x in items if x.category == 'security']),
                               my_server = len([x for x in items if x.category == 'server']),
                               my_support = len([x for x in items if x.category == 'support']),
                               my_unix = len([x for x in items if x.category == 'unix']),
                               my_windows = len([x for x in items if x.category == 'windows']),
                               all_communcation=len(all_communcation),
                               all_electronics = len(all_electronics),
                               all_hardware = len(all_hardware),
                               all_learning = len(all_learning),
                               all_mac = len(all_mac),
                               all_maintainance = len(all_maintainance),
                               all_networking = len(all_networking),
                               all_security = len(all_security),
                               all_server = len(all_server),
                               all_support = len(all_support),
                               all_unix = len(all_unix),
                               all_windows = len(all_windows)
                              )
    else:
        return redirect(url_for('home'))


@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('home'))