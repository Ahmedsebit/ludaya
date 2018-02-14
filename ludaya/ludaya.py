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
        user = User.query.filter_by(id=id).first()
        name = user.firstname + ' ' + user.lastname
        groups_list = []
        groups_list_opened = []
        for i in items:
            groups_list.append(i.category)
        groups = {x:groups_list.count(x) for x in groups_list}
        for i in opened_items:
            groups_list_opened.append(i.category)
        groups_opened = {x:groups_list_opened.count(x) for x in groups_list_opened}
        return render_template('index.html',
                               items=items,
                               groups=groups,
                               opened=groups_opened,
                               id=id,
                               name=name
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
        user = User.query.filter_by(id=id).first()
        name = user.firstname + ' ' + user.lastname
        my_task_category = category
        for task in tasks:
            task.tasks_id = task.name.replace(' ', '') + task.group.replace(' ', '')
        return render_template('open_tasks.html',
                                                tasks=tasks, 
                                                my_task_category=my_task_category, 
                                                id=id,
                                                name=name)
    else:
        return redirect(url_for('home'))

@app.route('/opened_tasks/<string:category>')
def started_tasks(category):
    if 'username' in session:
        username = session['username']
        id = session['id']
        tasks = AssignedTask.query.filter_by(user_id=id, category=category).all()
        user = User.query.filter_by(id=id).first()
        name = user.firstname + ' ' + user.lastname
        my_task_category = category
        for task in tasks:
            task.tasks_id = task.name.replace(' ', '') + task.group.replace(' ', '')
        return render_template('close_tasks.html', tasks=tasks, my_task_category=my_task_category, id=id, name=name)
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
        task.date_opened = db.func.current_timestamp()
        db.session.add(task)
        db.session.commit()
        my_task_category = task.category.upper()
        for task in tasks:
            task.tasks_id = task.name.replace(' ', '') + task.group.replace(' ', '')
        return redirect(url_for('issues'))
    else:
        return redirect(url_for('home'))


@app.route('/task/respond/<int:task_id>/', methods=['GET','POST'])
def respond_to_issue(task_id):
    if 'username' in session:
        username = session['username']
        id = session['id']
        if request.method == 'POST':
            user_id = session['id']
            task = AssignedTask.query.filter_by(id=task_id).first()
            task.user_answer = request.form['answer']
            task.date_resolved = db.func.current_timestamp()
            task.status = 'completed'
            db.session.add(task)
            db.session.commit()
            flash("Response sent")
            return redirect(url_for('issues'))
    else:
        return redirect(url_for('home'))


@app.route('/reports')
def reports():
    if 'username' in session:
        username = session['username']
        id = session['id']
        resolved_tasks = AssignedTask.query.filter_by(user_id=id, status='completed').all()
        opened_tasks = AssignedTask.query.filter_by(user_id=id, status='opened').all()
        user = User.query.filter_by(id=id).first()
        name = user.firstname + ' ' + user.lastname
        resolve_time = []
        response_time = []
        output_quality = []
        for resolved_task in resolved_tasks:
            start_dt = dt.datetime.strptime(str(resolved_task.date_resolved), '%Y-%m-%d %H:%M:%S.%f')
            end_dt = dt.datetime.strptime(str(resolved_task.date_created), '%Y-%m-%d %H:%M:%S.%f')
            resolution_diff = (start_dt - end_dt)
            resolution_total_time = resolution_diff.seconds/60 + resolution_diff.days*24*3600
            resolve_time.append(resolution_total_time/3600)
            output_quality.append(resolved_task.satisfaction)

        for opened_task in opened_tasks:
            opened_dt = dt.datetime.strptime(str(opened_task.date_opened), '%Y-%m-%d %H:%M:%S.%f')
            end_dt = dt.datetime.strptime(str(resolved_task.date_created), '%Y-%m-%d %H:%M:%S.%f')
            opened_diff = (opened_dt - end_dt) 
            opened_total_time = opened_diff.seconds/60 + opened_diff.days*24*3600
            response_time.append(opened_total_time/3600)
            

        if len(resolve_time) == 0:
            resolution_avarage_time = "No tasks yet"
        else:
            resolution_avarage_time = sum(resolve_time) / float(len(resolve_time))

        if len(response_time) == 0:
            resolution_avarage_time = "No tasks yet"
        else:
            response_avarage_time = sum(response_time) / float(len(response_time))

        try:
            user_satisfaction = sum(output_quality) / float(len(output_quality))
        except:
            user_satisfaction = "No tasks yet"
        

        lastsixmonths = last_six_months()

        
        return render_template('reports.html', 
                                task_count = len(resolved_tasks), 
                                resolution_avarage_time = math.ceil(resolution_avarage_time), 
                                response_avarage_time = math.ceil(response_avarage_time),
                                user_satisfaction = user_satisfaction,
                                lastsixmonths = json.dumps(lastsixmonths),
                                id=id,
                                name=name
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

@app.route('/api/new_tasks/<int:task_id>/open', methods=['POST'])
def post_open_tasks(task_id):
        task = AssignedTask.query.filter_by(id=task_id).first()
        if task:
            task.status = 'opened'
            task.date_opened = db.func.current_timestamp()
            db.session.add(task)
            db.session.commit()
            response = jsonify({
                                'id': task.id,
                                'name': task.name,
                                'date_created': task.date_created,
                                'status':task.status
                                })
        else:
            response = jsonify({'message': 'Item already exists in this bucketlist'})
            
        return response


@app.route('/api/opened_tasks/<string:category>/<int:id>', methods=['GET'])
def get_opened_tasks(category,id):
    tasks = AssignedTask.query.filter_by(user_id=id,  status="opened", category=category).all()
    items_result = assignedtasks_schema.dump(tasks)
    my_task_category = category.upper()
    for task in tasks:
        task.tasks_id = task.name.replace(' ', '') + task.group.replace(' ', '')
    return jsonify({
            'items':json.dumps(items_result.data)
    })


@app.route('/api/tasks/<string:category>/<int:id>', methods=['GET'])
def get_unopened_tasks(category,id):
    tasks = AssignedTask.query.filter_by(user_id=id,  status="not started", category=category).all()
    items_result = assignedtasks_schema.dump(tasks)
    my_task_category = category.upper()
    for task in tasks:
        task.tasks_id = task.name.replace(' ', '') + task.group.replace(' ', '')
    return jsonify({
            'items':json.dumps(items_result.data)
    })


@app.route('/api/reports/<int:id>', methods=['GET'])
def get_reports(id):
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
    
    
    return jsonify({'task_count':len(resolved_tasks), 
                    'resolution_avarage_time' : resolution_avarage_time, 
                    'response_avarage_time' : response_avarage_time,
                    'user_satisfaction' : user_satisfaction,
                    'lastsixmonths' : json.dumps(lastsixmonths),
    })
 

@app.route('/api/resolved_reports/<int:id>', methods=['GET'])
def resolved_report(id):
    resolved_tasks = AssignedTask.query.filter_by(user_id=id, status='completed').all()
    lastsixmonths = last_six_months()
    electronics = get_closed_user_monthly_tasks(resolved_tasks, 'electronics')
    hardware = get_closed_user_monthly_tasks(resolved_tasks, 'hardware')
    mac = get_closed_user_monthly_tasks(resolved_tasks, 'mac')
    maintainance = get_closed_user_monthly_tasks(resolved_tasks, 'maintainance')
    networking = get_closed_user_monthly_tasks(resolved_tasks, 'networking')
    security = get_closed_user_monthly_tasks(resolved_tasks, 'security')
    server = get_closed_user_monthly_tasks(resolved_tasks, 'server')
    support = get_closed_user_monthly_tasks(resolved_tasks, 'support')
    unix = get_closed_user_monthly_tasks(resolved_tasks, 'unix')
    windows = get_closed_user_monthly_tasks(resolved_tasks, 'windows')
    return jsonify({
            'lastsixmonths' : json.dumps(last_six_months()),
            'electronics': json.dumps(electronics),
            'hardware': json.dumps(hardware),
            'mac': json.dumps(mac),
            'maintainance': json.dumps(maintainance),
            'networking': json.dumps(networking),
            'security': json.dumps(security),
            'server': json.dumps(server),
            'support': json.dumps(support),
            'unix': json.dumps(unix),
            'windows': json.dumps(windows)
    })


@app.route('/api/opened_reports/<int:id>', methods=['GET'])
def opened_report(id):
    opened_tasks = AssignedTask.query.filter_by(user_id=id, status='opened').all()
    lastsixmonths = last_six_months()
    electronics = get_user_monthly_tasks(opened_tasks, 'electronics')
    hardware = get_user_monthly_tasks(opened_tasks, 'hardware')
    mac = get_user_monthly_tasks(opened_tasks, 'mac')
    maintainance = get_user_monthly_tasks(opened_tasks, 'maintainance')
    networking = get_user_monthly_tasks(opened_tasks, 'networking')
    security = get_user_monthly_tasks(opened_tasks, 'security')
    server = get_user_monthly_tasks(opened_tasks, 'server')
    support = get_user_monthly_tasks(opened_tasks, 'support')
    unix = get_user_monthly_tasks(opened_tasks, 'unix')
    windows = get_user_monthly_tasks(opened_tasks, 'windows')
    return jsonify({
            'lastsixmonths' : json.dumps(last_six_months()),
            'electronics': json.dumps(electronics),
            'hardware': json.dumps(hardware),
            'mac': json.dumps(mac),
            'maintainance': json.dumps(maintainance),
            'networking': json.dumps(networking),
            'security': json.dumps(security),
            'server': json.dumps(server),
            'support': json.dumps(support),
            'unix': json.dumps(unix),
            'windows': json.dumps(windows)
    })

@app.route('/api/satisfaction_reports/<int:id>')
def atisfaction_report(id):
    opened_tasks = AssignedTask.query.filter_by(user_id=id, status='completed').all()
    electronics = get_user_monthly_satisfaction(opened_tasks, 'electronics')
    hardware = get_user_monthly_satisfaction(opened_tasks, 'hardware')
    mac = get_user_monthly_satisfaction(opened_tasks, 'mac')
    maintainance = get_user_monthly_satisfaction(opened_tasks, 'maintainance')
    networking = get_user_monthly_satisfaction(opened_tasks, 'networking')
    security = get_user_monthly_satisfaction(opened_tasks, 'security')
    server = get_user_monthly_satisfaction(opened_tasks, 'server')
    support = get_user_monthly_satisfaction(opened_tasks, 'support')
    unix = get_user_monthly_satisfaction(opened_tasks, 'unix')
    windows = get_user_monthly_satisfaction(opened_tasks, 'windows')
    return jsonify({
            'lastsixmonths' : json.dumps(last_six_months()),
            'electronics': json.dumps(electronics),
            'hardware': json.dumps(hardware),
            'mac': json.dumps(mac),
            'maintainance': json.dumps(maintainance),
            'networking': json.dumps(networking),
            'security': json.dumps(security),
            'server': json.dumps(server),
            'support': json.dumps(support),
            'unix': json.dumps(unix),
            'windows': json.dumps(windows)
    })

    

@app.route('/api/time_reports/opened/<int:id>')
def opened_time_report(id):
    opened_tasks = AssignedTask.query.filter_by(user_id=id, status='opened').all()
    timeavarage = get_user_avarage_time(opened_tasks)
    return jsonify({
        'timeavarage':json.dumps(timeavarage)
    })

@app.route('/api/time_reports/closed/<int:id>')
def closed_time_report(id):
    resolved_tasks = AssignedTask.query.filter_by(user_id=id, status='completed').all()
    timeavarage = get_user_avarage_time_closed(resolved_tasks)
    return jsonify({
        'timeavarage':json.dumps(timeavarage)
    })


@app.route('/api/user_satisfaction_reports/<int:id>')
def user_satisfaction(id):
    resolved_tasks = AssignedTask.query.filter_by(user_id=id, status='completed').all()
    user_satisfactionavarage = get_user_avarage_satisfaction(resolved_tasks)
    return jsonify({
        'user_satisfactionavarage':json.dumps(user_satisfactionavarage)
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


@app.route('/api/user_monthly_tasks/')
def user_monthly_tasks():
    months = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    items = AssignedTask.query.filter_by(status="opened", user_id=19).all()
    for i in items:
        if i.date_opened is not None :
            if i.category == 'maintainance':
                months[dt.datetime.strptime(str(i.date_opened), '%Y-%m-%d %H:%M:%S.%f').month-1] += 1
    lastsixmonths = []
    currentMonth = dt.datetime.now().month
    if currentMonth < 6:
        remainingmonths = 6 - currentMonth
        for i in range(0, remainingmonths):
            lastsixmonths.append(months[-i-1])
        for i in range(0, currentMonth):
            lastsixmonths.append(months[i])
    if currentMonth == 6:
        for i in range(0, currentMonth):
            lastsixmonths.append(months[i])
    if currentMonth > 6:
        lastmonths = currentMonth - 6
        for i in range(lastmonths, currentMonth):
            lastsixmonths.append(months[i])
    return jsonify({
        'timeavarage':json.dumps(lastsixmonths)
    })

@app.route('/api/user_avarage_time/')
def user_avarage_time():
    items = AssignedTask.query.filter_by(status="completed", user_id=19).all()
    task_categories = ["maintainance", "networking", "windows", "communication", "support", "electonics", "server", "hardware", "unix", "security"]
    avarage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in items:
        start = i.date_created
        end = i.date_resolved
        start_dt = dt.datetime.strptime(str(start), '%Y-%m-%d %H:%M:%S.%f')
        end_dt = dt.datetime.strptime(str(end), '%Y-%m-%d %H:%M:%S.%f')
        diff = (end_dt - start_dt)
        avarage[task_categories.index(i.category)] += diff.seconds/60 + diff.days*24*3600
        avarage[task_categories.index(i.category)] = avarage[task_categories.index(i.category)] / 2
    return jsonify({
        'timeavarage':json.dumps(avarage)
    })