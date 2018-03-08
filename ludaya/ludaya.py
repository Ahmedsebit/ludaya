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
from notifications.mail import send_mail
from flask_marshmallow import Marshmallow

app = Flask(__name__)
Bootstrap(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
ma = Marshmallow(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ahmedamedy@gmail.com'
app.config['MAIL_PASSWORD'] = 'osmantito88'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

db = SQLAlchemy(app)

from models import User, AssignedTask, assignedtask_schema, assignedtasks_schema, Groups
from tasks.task_reports import last_six_months, get_user_monthly_tasks, get_user_monthly_satisfaction, get_user_avarage_time, get_user_avarage_satisfaction, get_closed_user_monthly_tasks, get_user_avarage_time_closed
from random import randrange

from notifications.slack import send_channel_messages

@app.route('/issues')
def issues():
    if 'username' in session:
        username = session['username']
        id = session['id']
        items = AssignedTask.query.filter_by(status="not started", user_id=id).all()
        completed_items = AssignedTask.query.filter_by(status="completed", user_id=id).all()
        opened_items = AssignedTask.query.filter_by(status="opened", user_id=id).all()
        user = User.query.filter_by(id=id).first()
        user_group = Groups.query.filter_by(id=user.group).first()
        team_leader = User.query.filter_by(id=user_group.team_lead).first()
        name = user.firstname + ' ' + user.lastname
        team_lead_names = team_leader.firstname + ' ' + team_leader.lastname
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
                               name=name,
                               teamlead_name=team_lead_names,
                              )
    else:
        return redirect(url_for('user.home'))


@app.route('/portfolio')
def portfolio():
    if 'username' in session:
        username = session['username']
        id = session['id']
        items = AssignedTask.query.filter_by(status="not started", user_id=id).all()
        user = User.query.filter_by(id=items.user_id)
        
        return render_template('portfolio.html', 
                                id=id,
                                firstName=user.firstname,
                                secondName=user.lastname)
    else:
        return redirect(url_for('user.home'))


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
        return redirect(url_for('user.home'))


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
        return redirect(url_for('user.home'))

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
        return redirect(url_for('user.home'))


@app.route('/new_tasks/<int:task_id>/open', methods=['POST'])
def open_tasks(task_id):
    if 'username' in session:
        username = session['username']
        id = session['id']
        user = User.query.filter_by(id=id).first()
        task = AssignedTask.query.filter_by(id=task_id).first()
        group = Groups.query.filter_by(id=user.group).first()
        task.status = 'opened'
        task.date_opened = db.func.current_timestamp()
        db.session.add(task)
        db.session.commit()

        # message = ' *'+'Task Opened'+'*\n'+'```'+'By:'+user.firstname.lower().title()+' '+ user.lastname.lower().title() +'\n'+task.name+'```'
        # send_channel_messages(group.name, message)
        flash('You have opened a new task')
        return redirect(url_for('issues'))
    else:
        return redirect(url_for('user.home'))


@app.route('/new_tasks/<int:task_id>/close', methods=['POST'])
def close_task(task_id):
    if 'username' in session:
        username = session['username']
        id = session['id']
        if request.method == 'POST':
            user_id = session['id']
            user = User.query.filter_by(id=id).first()
            task = AssignedTask.query.filter_by(id=task_id).first()
            group = Groups.query.filter_by(id=user.group).first()
            team_lead = User.query.filter_by(id=group.team_lead).first()
            task.user_answer = request.form['answer']
            
            task.date_resolved = db.func.current_timestamp()
            task.status = 'completed'
            db.session.add(task)
            db.session.commit()

            message = ' *'+'Task Closed'+'*\n'+'```'+'By:'+user.firstname.lower().title()+' '+ user.lastname.lower().title() +'\n'+task.name+'```'
            # send_channel_messages(group.name, message)
            task_message = task.name + '\n' + 'Closed by: ' + user.firstname + ' ' + user.lastname

            send_mail("New Tasks Closed", 'notification@ludaya.com', [team_lead.email], task_message)

            flash("The task has been closed")
            return redirect(url_for('issues'))
    else:
        return redirect(url_for('user.home'))


@app.route('/new_tasks/<int:task_id>/evaluate', methods=['POST'])
def evaluate_new_task(task_id):
    if 'username' in session:
        username = session['username']
        id = session['id']
        if request.method == 'POST':
            user_id = session['id']
            user = User.query.filter_by(id=id).first()
            task = AssignedTask.query.filter_by(id=task_id).first()
            group = Groups.query.filter_by(id=user.group).first()

            task.evaluate_comment = request.form['comment']
            task.satisfaction = float(request.form['rating'])
            task.date_resolved = db.func.current_timestamp()
            task.evaluated_status = 'evaluated'

            task_owner = User.query.filter_by(id=task.user_id).first()
            db.session.add(task)
            db.session.commit()

            # message = ' *'+'Task Evaluated'+'*\n'+'```'+'By:'+user.firstname.lower().title()+' '+ user.lastname.lower().title() +'\n'+task.name+'```'
            # send_channel_messages(group.name, message)
            task_message = task.name + '\n' + 'Evaluated by: ' +user.firstname + ' ' + user.lastname
            send_mail("New Tasks Evaluated", 'notification@ludaya.com', [task_owner.email], task_message)

            flash("the task has been evaluated")
            return redirect(url_for('issues'))
    else:
        return redirect(url_for('user.home'))


@app.route('/evaluate_tasks/<string:category>')
def evaluate_tasks(category):
    if 'username' in session:
        username = session['username']
        id = session['id']
        tasks = AssignedTask.query.filter_by(user_id=id, category=category).all()
        user = User.query.filter_by(id=id).first()
        name = user.firstname + ' ' + user.lastname
        my_task_category = category
        for task in tasks:
            task.tasks_id = task.name.replace(' ', '') + task.group.replace(' ', '')
        return render_template('evaluate_tasks.html',
                                                tasks=tasks, 
                                                my_task_category=my_task_category, 
                                                id=id,
                                                name=name)
    else:
        return redirect(url_for('user.home'))


@app.route('/completed_tasks/<string:category>')
def completed_tasks(category):
    if 'username' in session:
        username = session['username']
        id = session['id']
        tasks = AssignedTask.query.filter_by(user_id=id, category=category).all()
        user = User.query.filter_by(id=id).first()
        name = user.firstname + ' ' + user.lastname
        my_task_category = category
        for task in tasks:
            task.tasks_id = task.name.replace(' ', '') + task.group.replace(' ', '')
        return render_template('completed_tasks.html',
                                                tasks=tasks, 
                                                my_task_category=my_task_category, 
                                                id=id,
                                                name=name)
    else:
        return redirect(url_for('user.home'))


@app.route('/reports')
def reports():
    if 'username' in session:
        username = session['username']
        id = session['id']
        resolved_tasks = AssignedTask.query.filter_by(user_id=id, status='completed').all()
        evaluated_tasks = AssignedTask.query.filter_by(user_id=id, evaluated_status='evaluated').all()
        opened_tasks = AssignedTask.query.filter_by(user_id=id, status='opened').all()
        user = User.query.filter_by(id=id).first()
        name = user.firstname + ' ' + user.lastname
        resolve_time = []
        response_time = []
        output_quality = []

        
        for resolved_task in resolved_tasks:
            start_dt = dt.datetime.strptime(str(resolved_task.date_resolved), '%Y-%m-%d %H:%M:%S.%f')
            end_dt = dt.datetime.strptime(str(resolved_task.date_created), '%Y-%m-%d %H:%M:%S.%f')
            res_dt = dt.datetime.strptime(str(resolved_task.date_opened), '%Y-%m-%d %H:%M:%S.%f')
            resolution_diff = (start_dt - end_dt)
            resolution_total_time = resolution_diff.seconds/60 + resolution_diff.days*24*3600
            resolve_time.append(resolution_total_time)
            
            resp_diff = (res_dt - end_dt)
            resp_total_time = resp_diff.seconds/60 + resp_diff.days*24*60
            response_time.append(resp_total_time)
            
        for task in evaluated_tasks:
            output_quality.append(task.satisfaction)

        for opened_task in opened_tasks:
            opened_dt = dt.datetime.strptime(str(opened_task.date_opened), '%Y-%m-%d %H:%M:%S.%f')
            end_dt = dt.datetime.strptime(str(opened_task.date_created), '%Y-%m-%d %H:%M:%S.%f')
            opened_diff = (opened_dt - end_dt) 
            opened_total_time = opened_diff.seconds/60 + opened_diff.days*24*60
            response_time.append(opened_total_time)

        if len(resolve_time) == 0:
            resolution_avarage_time = 0
        else:
            resolution_avarage_time = sum(resolve_time) / float(len(resolve_time))

        if len(response_time) == 0:
            response_avarage_time = 0
        else:
            response_avarage_time = sum(response_time) / float(len(response_time))

        if len(output_quality) == 0:
            user_satisfaction = 0
        else:
            user_satisfaction = sum(output_quality) / float(len(output_quality))
        
        lastsixmonths = last_six_months()
        return render_template('reports.html', 
                                task_count = len(resolved_tasks), 
                                resolution_avarage_time = resolution_avarage_time, 
                                response_avarage_time = response_avarage_time,
                                user_satisfaction = user_satisfaction,
                                lastsixmonths = json.dumps(lastsixmonths),
                                id=id,
                                name=name
                                )
    else:
        return redirect(url_for('user.home'))

