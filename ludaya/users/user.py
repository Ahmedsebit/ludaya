from flask import Flask, render_template, session, flash, request, redirect, url_for, flash, jsonify, \
                Blueprint, g, redirect, abort, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import string
import random
from validate_email import validate_email
from ludaya import app
from models import User, Groups, AssignedTask, assignedtask_schema, assignedtasks_schema
from random import randrange
from groups import create_group, get_last_created_group
from notifications.mail import send_mail
from notifications.slack import add_user_to_channel, get_channel_id, get_user

user_blueprint = Blueprint(
    'user',__name__,
    template_folder = 'templates',
    static_folder='static'
)
db = SQLAlchemy(app)


@user_blueprint.route('/')
def home():
    if 'username' in session:
        username = session['username']
        id = session['id']
        return redirect(url_for('issues'))
    else:
        return render_template('home.html')


@user_blueprint.route('/register', methods=['POST'])
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
                        user.save()
                        user = User.query.filter_by(email=email).first()
                        new_group = create_group(user.id)
                        user.group = new_group.id
                        user.save()
                        channel = get_channel_id(new_group.name)
                        user = get_user(user.email)
                        add_user_to_channel(channel, user)
                    if lastgroup.current_members < 4:
                        lastgroup.current_members += 1
                        lastgroup.save()
                        user = User(firstname=firstname, lastname=lastname, email=email, group=lastgroup.id)
                        user.hash_password(password)
                        user.save()
                        user = User.query.filter_by(email=email).first()
                        channel = get_channel_id(lastgroup.name)
                        user = get_user(user.email)
                        add_user_to_channel(channel, user)
                else:
                    user = User(firstname=firstname, lastname=lastname, email=email)
                    user.hash_password(password)
                    user.save()
                    db.session.refresh(user)
                    new_group = create_group(user.id)
                    user.group = new_group.id
                    user.save()
                    user = User.query.filter_by(email=email).first()
                    channel = get_channel_id(new_group.name)
                    user = get_user(user.email)
                    add_user_to_channel(channel, user)

                flash('You were successfully register')
                return redirect(url_for('user.home'))
        else:
            error = 'User already exists'
    else:
        error = 'Invalid email'
    return render_template('home.html', error=error)


@user_blueprint.route('/login', methods=['POST'])
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


@user_blueprint.route('/forgotpassword', methods=['POST'])
def forgotpassword():
    '''
    Function for user forgot password
    '''
    try:
        user = User.query.filter_by(email=request.form['email']).first()
        if user:
            password = id_generator()
            user.hash_password(password)
            user.save()
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
        error = 'Email not found!!'
        return render_template('home.html', error=error)

@user_blueprint.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('user.home'))

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

