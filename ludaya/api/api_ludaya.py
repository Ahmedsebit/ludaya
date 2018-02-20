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

from tasks.usertask import allocate_all_user_tasks, testing, get_user_tasks
from tasks.tasksallocations import get_user_assigned_tasks, electronics_task, hardware_task, mac_task, maintainance_task, networking_task, security_task, server_task, software_task, support_task, unix_task, windows_task
from random import randrange


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


@app.route('/api/assign_task/')
def assign_task():
    main_random_index = randrange(0, len(networking))
    task = networking[main_random_index]
    task_category = task['name']
    random_index = randrange(0, len(task['tasklist']))
    selected_task = task['tasklist'][random_index]
    new_task = {task_category:selected_task}

    category_list = get_user_assigned_tasks(1, 'networking')
    categiory_in_db_list = [i['name'] for i in category_list]

    if task['name'] in categiory_in_db_list:
        if selected_task not in task['tasklist']:
            new_task = {task_category:selected_task}
        else:
            random_index = randrange(0, len(task['tasklist']))
    else:
        new_task = {task_category:selected_task}
    
    return jsonify({
        'task_list':json.dumps(new_task)
    })


@app.route('/api/assigned_task/')
def get_assigned_tasks():
    tasks = AssignedTask.query.filter_by(category='mac', user_id=19)
    task_list = []
    task_name = []
    for task in tasks:
        task_name.append(task.group)
        if len(task_list)>0:
            for i in task_list:
                if i['name'] in task_name:
                    if i['name'] == task.group and task.name not in i['tasklist']:
                        i['tasklist'].append(task.name)
                else:
                    task_list.append({'name':task.group, 'tasklist':[task.name]})
        else:
            task_list.append({'name':task.group, 'tasklist':[task.name]})
    return jsonify({
        'task_list':json.dumps(task_list)
    })

