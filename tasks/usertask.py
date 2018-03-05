# coding: utf8

import os
from flask_sqlalchemy import SQLAlchemy
from decorators import async
from models import AssignedTask, User, Groups
from ludaya.ludaya import db
from datetime import datetime, time
from tasks.tasksallocations import category_task
from notifications.slack import send_channel_messages, send_dm
from notifications.mail import send_mail

def allocate_all_user_tasks():
    now = datetime.now()
    now_time = now.time()
    if now_time >= time(10,30) and now_time <= time(14,30):
        async_allocate_all_user_tasks()

@async
def async_allocate_all_user_tasks():
    users = User.query.all()
    for user in users:
        group = Groups.query.filter_by(id = user.group).first()
        all_tasks = category_task(user.id)
        tasks = []
        for task in all_tasks:
            if group.team_lead != user.id:
                task_group = task.keys()[0]
                name = task[task_group]
                tasks.append(name)
                tasks.append('\n')
                allocate(task, user.id, user.email, group.team_lead)

        task_strng = ""

        for i in tasks:
            task_strng +=str(i)

        if len(tasks) > 0:
            # message = ' *'+'New Task'+'*\n'+'```'+'Asigned to:'+user.firstname.lower().title()+' '+ user.lastname.lower().title() +'\n'+task_strng+'```'
            send_mail('New Assigned Task', 'notifications@ludaya.com', [user.email], task_strng)


def allocate(task, user, email, team_lead):
    category = task['name']
    group = task.keys()[0]
    name = task[group]
    if category != name:
        new_task = AssignedTask(name=name, group=group, category=category, user_id=user, evaluate_id = team_lead)
        db.session.add(new_task)
        db.session.commit()


def get_user_tasks(user_id):
    tasks = AssignedTask.get_assignedtask(user_id)
    lst = []
    for task in tasks:
        lst.append(task)
    return lst
