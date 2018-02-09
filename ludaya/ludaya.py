from flask import Flask, render_template, session, flash, request, redirect, url_for, flash, jsonify, \
                Blueprint, g, redirect, abort, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import json
import os
import re
import string
import random
import datetime as dt
from validate_email import validate_email
from flask_bootstrap import Bootstrap
from tasks.alltasks import communcation_list_length, electronics_list_length, hardware_list_length, learning_list_length, mac_list_length, maintainance_list_length, networking_list_length, security_list_length, server_list_length, support_list_length, unix_list_length, windows_list_length
from tasks.alltasks import communication, electronics, hardware, mac, maintainance, networking, security, server, support, unix, windows
from tasks.task_reports import last_six_months, get_user_monthly_tasks, get_user_monthly_satisfaction, get_user_avarage_time, get_user_avarage_satisfaction

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

from models import User, AssignedTask, assignedtask_schema, assignedtasks_schema


@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
        id = session['id']
        return redirect(url_for('issues'))
    else:
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
            confirmpassword = request.form['confirmpassword']
            if email is None or password is None:
                error = 'Empty email or password'
            elif password != confirmpassword:
                error = 'Passwords do not match'
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
            send_mail(heading, sender, recepients, message)
            error = 'Password sent'
            return render_template('home.html', error=error)
        else:
            error = 'Invalid email, Please try again.'
            return render_template('home.html', error=error)
    except:
        error = 'No email field!!'
        return render_template('home.html', error=error)


@app.route('/issues')
def issues():
    if 'username' in session:
        username = session['username']
        id = session['id']
        items = AssignedTask.query.filter_by(status="not started", user_id=id).all()
        completed_items = AssignedTask.query.filter_by(status="completed", user_id=id).all()
        opened_items = AssignedTask.query.filter_by(status="opened", user_id=id).all()
        groups_list = []
        groups_list_opened = []
        for i in items:
            groups_list.append(i.category)
        groups = {x:groups_list.count(x) for x in groups_list}
        for i in opened_items:
            groups_list_opened.append(i.category)
        groups_opened = {x:groups_list_opened.count(x) for x in groups_list_opened}
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

        return render_template('issues.html',
                               items=items,
                               groups=groups,
                               opened=groups_opened,
                               id=id,
                               my_communication=len([x for x in completed_items if x.category == 'communication']),
                               my_electronics=len([x for x in completed_items if x.category == 'electronics']),
                               my_hardware=len([x for x in completed_items if x.category == 'hardware']),
                               my_learning= len([x for x in completed_items if x.category == 'learning']),
                               my_mac = len([x for x in completed_items if x.category == 'communication']),
                               my_maintainance = len([x for x in completed_items if x.category == 'maintainance']),
                               my_networking = len([x for x in completed_items if x.category == 'networking']),
                               my_security = len([x for x in completed_items if x.category == 'security']),
                               my_server = len([x for x in completed_items if x.category == 'server']),
                               my_support = len([x for x in completed_items if x.category == 'support']),
                               my_unix = len([x for x in completed_items if x.category == 'unix']),
                               my_windows = len([x for x in completed_items if x.category == 'windows']),
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


@app.route('/new_tasks/<string:category>')
def tasks(category):
    if 'username' in session:
        username = session['username']
        id = session['id']
        tasks = AssignedTask.query.filter_by(user_id=id, category=category).all()
        my_task_category = category.upper()
        for task in tasks:
            task.tasks_id = task.name.replace(' ', '') + task.group.replace(' ', '')
        return render_template('unopened_tasks.html', tasks=tasks, my_task_category=my_task_category)
    else:
        return redirect(url_for('home'))


@app.route('/tasks/<string:category>')
def opened_tasks(category):
    if 'username' in session:
        username = session['username']
        id = session['id']
        tasks = AssignedTask.query.filter_by(user_id=id, category=category).all()
        my_task_category = category.upper()
        for task in tasks:
            task.tasks_id = task.name.replace(' ', '') + task.group.replace(' ', '')
        return render_template('tasks.html', tasks=tasks, my_task_category=my_task_category)
    else:
        return redirect(url_for('home'))


@app.route('/new_tasks/<int:task_id>/open', methods=['POST'])
def open_tasks(task_id):
    if 'username' in session:
        username = session['username']
        id = session['id']
        task = AssignedTask.query.filter_by(id=task_id).first()
        tasks = AssignedTask.query.filter_by(user_id=id, category='communication').all()
        task.status = 'opened'
        db.session.add(task)
        db.session.commit()
        my_task_category = task.category.upper()
        for task in tasks:
            task.tasks_id = task.name.replace(' ', '') + task.group.replace(' ', '')
        return render_template('tasks.html', tasks=tasks, my_task_category=my_task_category)
    else:
        return redirect(url_for('home'))


@app.route('/reports')
def reports():
    if 'username' in session:
        username = session['username']
        id = session['id']
        resolved_tasks = AssignedTask.query.filter_by(user_id=id, status='resolved').all()
        opened_tasks = AssignedTask.query.filter_by(user_id=id, status='opened').all()
        time = []
        output_quality = []
        for resolved_task in resolved_tasks:
            if resolved_task.date_resolved is None:
                pass
            else:
                start=resolved_task.date_resolved
                opened=resolved_task.date_opened
                end=resolved_task.date_created
                start_dt = dt.datetime.strptime(start, '%Y-%m-%d %H:%M:%S.%f')
                end_dt = dt.datetime.strptime(end, '%Y-%m-%d %H:%M:%S.%f')
                opened_dt = dt.datetime.strptime(opened, '%Y-%m-%d %H:%M:%S.%f')
                opened_diff = (opened_dt - start_dt) 
                opened_total_time = opened_diff.seconds/60 + opened_diff.days*24*3600
                time.append(opened_total_time)
                resolution_diff = (end_dt - start_dt) 
                resolution_total_time = resolution_diff.seconds/60 + resolution_diff.days*24*3600
                time.append(resolution_total_time)
                time.append(resolved_task.satisfaction)
        try:
            resolution_avarage_time = sum(time) / float(len(time))
            response_avarage_time = sum(time) / float(len(time))
            user_satisfaction = sum(output_quality) / float(len(output_quality))
        except:
            resolution_avarage_time = "No tasks yet"
            response_avarage_time = "No tasks yet"
            user_satisfaction = "No tasks yet"

            lastsixmonths = last_six_months()
        
        
        return render_template('reports.html', 
                                task_count = len(resolved_tasks), 
                                resolution_avarage_time = resolution_avarage_time, 
                                response_avarage_time = response_avarage_time,
                                user_satisfaction = user_satisfaction,
                                lastsixmonths = json.dumps(lastsixmonths),
                                maintainancelastsixmonths = json.dumps(get_user_monthly_tasks(resolved_tasks, 'maintainance')),
                                networkinglastsixmonths = json.dumps(get_user_monthly_tasks(resolved_tasks, 'networking')),
                                windowslastsixmonths = json.dumps(get_user_monthly_tasks(resolved_tasks, 'windows')),
                                communicationlastsixmonths = json.dumps(get_user_monthly_tasks(resolved_tasks, 'communication')),
                                supportlastsixmonths = json.dumps(get_user_monthly_tasks(resolved_tasks, 'support')),
                                electonicslastsixmonths = json.dumps(get_user_monthly_tasks(resolved_tasks, 'electronics')),
                                serverlastsixmonths = json.dumps(get_user_monthly_tasks(resolved_tasks, 'server')),
                                hardwarelastsixmonths = json.dumps(get_user_monthly_tasks(resolved_tasks, 'hardware')),
                                unixlastsixmonths = json.dumps(get_user_monthly_tasks(resolved_tasks, 'unix')),
                                securitylastsixmonths = json.dumps(get_user_monthly_tasks(resolved_tasks, 'security')),
                                openedmaintainancelastsixmonths = json.dumps(get_user_monthly_tasks(opened_tasks, 'maintainance')),
                                openednetworkinglastsixmonths = json.dumps(get_user_monthly_tasks(opened_tasks, 'networking')),
                                openedwindowslastsixmonths = json.dumps(get_user_monthly_tasks(opened_tasks, 'windows')),
                                openedcommunicationlastsixmonths = json.dumps(get_user_monthly_tasks(opened_tasks, 'communication')),
                                openedsupportlastsixmonths = json.dumps(get_user_monthly_tasks(opened_tasks, 'support')),
                                openedelectonicslastsixmonths = json.dumps(get_user_monthly_tasks(opened_tasks, 'electronics')),
                                openedserverlastsixmonths = json.dumps(get_user_monthly_tasks(opened_tasks, 'server')),
                                openedhardwarelastsixmonths = json.dumps(get_user_monthly_tasks(opened_tasks, 'hardware')),
                                openedunixlastsixmonths = json.dumps(get_user_monthly_tasks(opened_tasks, 'unix')),
                                openedsecuritylastsixmonths = json.dumps(get_user_monthly_tasks(opened_tasks, 'security')),
                                outputmaintainancelastsixmonths = json.dumps(get_user_monthly_satisfaction(opened_tasks, 'maintainance')),
                                outputnetworkinglastsixmonths = json.dumps(get_user_monthly_satisfaction(opened_tasks, 'networking')),
                                outputwindowslastsixmonths = json.dumps(get_user_monthly_satisfaction(opened_tasks, 'windows')),
                                outputcommunicationlastsixmonths = json.dumps(get_user_monthly_satisfaction(opened_tasks, 'communication')),
                                outputsupportlastsixmonths = json.dumps(get_user_monthly_satisfaction(opened_tasks, 'support')),
                                outputelectonicslastsixmonths = json.dumps(get_user_monthly_satisfaction(opened_tasks, 'electronics')),
                                outputserverlastsixmonths = json.dumps(get_user_monthly_satisfaction(opened_tasks, 'server')),
                                outputhardwarelastsixmonths = json.dumps(get_user_monthly_satisfaction(opened_tasks, 'hardware')),
                                outputunixlastsixmonths = json.dumps(get_user_monthly_satisfaction(opened_tasks, 'unix')),
                                outputsecuritylastsixmonths = json.dumps(get_user_monthly_satisfaction(opened_tasks, 'security')),
                                responsetimeavarage = json.dumps(get_user_avarage_time(resolved_tasks, 'date_opened')),
                                resolutiontimeavarage = json.dumps(get_user_avarage_time(resolved_tasks, 'date_resolved')),
                                user_satisfactionavarage = json.dumps(get_user_avarage_satisfaction(resolved_tasks))
                                )
    else:
        return redirect(url_for('home'))

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


@app.route('/api/issues/<string:category>/<int:id>', methods=['GET'])
def get_all_category(category, id):
    completed_items = AssignedTask.query.filter_by(status="completed", category =category, user_id=id).all()
    opened_items = AssignedTask.query.filter_by(status="opened",  category =category, user_id=id).all()
    
    all = list_length(category)
    
    return jsonify({'completed':len(completed_items),
                    'opened':len(opened_items),
                    'all':len(all)}
                    )

@app.route('/api/issues/<int:id>', methods=['GET'])    
def get_issues(id):
    items = AssignedTask.query.filter_by(status="not started", user_id=id).all()
    items_result = assignedtasks_schema.dump(items)
    completed_items = AssignedTask.query.filter_by(status="completed", user_id=id).all()
    opened_items = AssignedTask.query.filter_by(status="opened", user_id=id).all()
    groups_list = []
    groups_list_opened = []
    for i in items:
        groups_list.append(i.category)
    groups = {x:groups_list.count(x) for x in groups_list}
    for i in opened_items:
        groups_list_opened.append(i.category)
    groups_opened = {x:groups_list_opened.count(x) for x in groups_list_opened}
    return jsonify({
            'items':json.dumps(items_result.data),
            'groups':json.dumps(groups),
            'opened':json.dumps(groups_opened)
    })

@app.route('/api/opened_issues/<int:id>', methods=['GET'])    
def get_opened_issues(id):
    items = AssignedTask.query.filter_by(status="opened", user_id=id).all()
    items_result = assignedtasks_schema.dump(items)
    completed_items = AssignedTask.query.filter_by(status="completed", user_id=id).all()
    opened_items = AssignedTask.query.filter_by(status="opened", user_id=id).all()
    groups_list = []
    groups_list_opened = []
    for i in items:
        groups_list.append(i.category)
    groups = {x:groups_list.count(x) for x in groups_list}
    for i in opened_items:
        groups_list_opened.append(i.category)
    groups_opened = {x:groups_list_opened.count(x) for x in groups_list_opened}
    return jsonify({
            'items':json.dumps(items_result.data),
            'groups':json.dumps(groups),
            'opened':json.dumps(groups_opened)
    })


@app.route('/api/tasks/<string:category>/<int:id>')
def get_opened_tasks(category,id):
    # if 'username' in session:
    #     username = session['username']
    #     id = session['id']
    tasks = AssignedTask.query.filter_by(user_id=id, category=category).all()
    items_result = assignedtasks_schema.dump(tasks)
    my_task_category = category.upper()
    for task in tasks:
        task.tasks_id = task.name.replace(' ', '') + task.group.replace(' ', '')
    return jsonify({
            'items':json.dumps(items_result.data)
    })


def list_length(category):
    all = [
        {'communication': communication},
        {'electronics': electronics},
        {'hardware': hardware},
        {'mac': mac},
        {'maintainance': maintainance},
        {'networking': networking},
        {'security': security},
        {'server': server},
        {'support': support},
        {'unix': unix},
        {'windows': windows}
    ]
    l = []
    for item in all:
        for key, value in item.items():
            if key == category:
                for i in value:
                    for j in i.values()[0]:
                        l.append(j)

    return l

