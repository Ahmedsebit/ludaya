import os
from decorators import async

from flask_sqlalchemy import SQLAlchemy

from models import AssignedTask, User
from ludaya.ludaya import db
from datetime import date

from notifications.mail import send_mail

from tasks.socialmedia_administrator.socialmedia_administrator import SOCIALMEDIA_ADMINISTRATOR as socialmedia_administrator

from random import randrange
import random


all_tasks = [
            {'socialmedia_administrator':socialmedia_administrator}
]


def dow(date):
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    dayNumber=date.weekday()
    return days[dayNumber]


def get_user_assigned_tasks(user_id, category):
    category_tasks = AssignedTask.query.filter_by(category=category, user_id=user_id).all()
    assigned_category_tasks = [category_task.name for category_task in category_tasks]
    return assigned_category_tasks


def get_category_length():
    tasks = []
    # for category_item in category:
    for category_item in all_tasks[0].values():
        for item in category_item[0]['tasklist']:
            tasks.append(item)
    print(tasks)
    return tasks


def get_new_task(category_name, category):
    today = dow(date.today())
    # if today != "Sunday" or today != "Saturday":
    selected_category = random.choice(category)
    selected_task = random.choice(selected_category)
    selected_task_group = selected_task['name']
    selected_task_name = random.choice(selected_task['tasklist'])

    new_task = {
                'task_name':selected_task_name,
                'task_category':category_name,
                'task_group':selected_task_group
                }
    return new_task


def save_task(name, group, category, user):
    new_task = AssignedTask(name=name, group=group, category=category, user_id=user)
    db.session.add(new_task)
    db.session.commit()


def notify(email, tasks):
    task_strng = ""
    for i in tasks:
        task_strng +=str(i)
    if len(tasks) > 0:
            send_mail('New Assigned Task', 'notifications@ludaya.com', [email], task_strng)


def format_email(tasks):
    tasks.append('\n')
    tasks.append('Thank you')
    tasks.append('\n')
    tasks.append('\n')
    tasks.append('Ludaya Team')
    tasks.insert(0, '\n')
    tasks.insert(0, '\n')
    tasks.insert(0, 'You have been assigned the following tasks:')
    tasks.insert(0, '\n')
    tasks.insert(0, '\n')
    tasks.insert(0, 'Greeting')

    return tasks


def assign_socalmedia_admin_task():
    users = User.query.filter_by(job_description='socialmedia_administrator').all()
    if users:
        for user in users:
            tasks = []
            for task in all_tasks:
                new_task = get_new_task(task.keys(), task.values())
                save_task(new_task['task_name'], new_task['task_group'], new_task['task_category'], user.id)
                tasks.append(new_task['task_name'])
                tasks.append('\n')
            tasks = format_email(tasks)
            notify(user.email, tasks)

