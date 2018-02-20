from flask import Flask, render_template, session, flash, request, redirect, url_for, flash, jsonify, \
                Blueprint, g, redirect, abort, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import json
import os
import re
import string
import random
import math
import datetime as dt
from validate_email import validate_email
from flask_bootstrap import Bootstrap
from tasks.alltasks import communcation_list_length, electronics_list_length, hardware_list_length, learning_list_length, mac_list_length, maintainance_list_length, networking_list_length, security_list_length, server_list_length, support_list_length, unix_list_length, windows_list_length
from tasks.alltasks import communication, electronics, hardware, mac, maintainance, networking, security, server, support, unix, windows
from tasks.task_reports import last_six_months, get_user_monthly_tasks, get_user_monthly_satisfaction, get_user_avarage_time, get_user_avarage_satisfaction, get_closed_user_monthly_tasks, get_user_avarage_time_closed

from flask_marshmallow import Marshmallow

app = Flask(__name__)
Bootstrap(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
ma = Marshmallow(app)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ahmedamedy@gmail.com'
app.config['MAIL_PASSWORD'] = 'osmantito88'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

db = SQLAlchemy(app)

from models import User, Groups, AssignedTask, assignedtask_schema, assignedtasks_schema
from random import randrange
from groups import create_group, get_last_created_group

@app.route('/register', methods=['POST'])
def register():
    is_valid = validate_email(request.form['email'])
    error = None
    if is_valid:
        user = User.query.filter_by(email=request.form['email']).first()
        lastgroup = get_last_created_group()
        if not user:
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            password = request.form['password']
            confirmpassword = request.form['confirmpassword']
            if email is None or password is None:
                error = 'Empty email or password'
            elif password != confirmpassword:
                error = 'Passwords do not match'
            else:
                if lastgroup:
                    if lastgroup.current_members == 4:
                        user = User(firstname=firstname, lastname=lastname, email=email)
                        user.hash_password(password)
                        db.session.add(user)
                        db.session.commit()
                        db.session.refresh(user)
                        new_group = create_group(user.id)
                        user.group = new_group.id
                        db.session.add(user)
                        db.session.commit()
                    if lastgroup.current_members < 4:
                        lastgroup.current_members += 1
                        db.session.add(lastgroup)
                        db.session.commit(lastgroup)
                        user = User(firstname=firstname, lastname=lastname, email=email, group=lastgroup.id)
                        user.hash_password(password)
                        db.session.add(user)
                        db.session.commit()     
                else:
                    create_group(user.id)
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


@app.route('/forgotpassword', methods=['POST'])
def forgotpassword():
    '''
    Function for user forgot password
    '''
    try:
        user = User.query.filter_by(email=request.form['email']).first()
        if user:
            password = id_generator()
            user.hash_password(password)
            db.session.add(user)
            db.session.commit()
            heading = 'Password Reset'
            sender = 'ahmedamedy@gmail.com'
            recipients = [user.email]
            message = "Your email password has been reset to: "+password
            send_mail(heading, sender, recipients, message)
            error = 'Password sent'
            return render_template('home.html', error=error)
        else:
            error = 'Invalid email, Please try again.'
            return render_template('home.html', error=error)
    except:
        error = 'No email field!!'
        return render_template('home.html', error=error)

@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('home'))

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def send_mail(heading, sender, recepients, message):
   msg = Message(heading, sender = sender, recipients = recepients)
   msg.body = message
   mail.send(msg)
   return "Sent"