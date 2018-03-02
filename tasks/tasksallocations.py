import os
from decorators import async

from flask_sqlalchemy import SQLAlchemy

from models import AssignedTask, User
from ludaya.ludaya import db
from datetime import date

from software import SOFTWARE as softwares
from electronics import ELECTRONICS as electronics
from hardware import HARDWARE as hardwares
from mac import MAC as macs
from maintainance import MAINTAINANCE as maintainances
from networking import NETWORKING as networkings
from security import SECURITY as securities
from server import SERVER as servers
from support import SUPPORT as supports
from unix import UNIX as unixs
from windows import WINDOWS as windows

from random import randrange


def dow(date):
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    dayNumber=date.weekday()
    return days[dayNumber]

def get_user_assigned_tasks(user_id, category):
    tasks = AssignedTask.query.filter_by(category=category, user_id=user_id)
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
    return task_list

def assign_task(user_id, category_name, category):
    today = dow(date.today())
    # if today != "Sunday" or today != "Saturday":
    main_random_index = randrange(0, len(category))
    task = category[main_random_index]
    task_category = task['name']
    random_index = randrange(0, len(task['tasklist']))
    selected_task = task['tasklist'][random_index]
    new_task = {task_category:selected_task}

    category_list = get_user_assigned_tasks(user_id, category_name)
    categiory_in_db_list = [i['name'] for i in category_list]

    if task['name'] in categiory_in_db_list:
        if selected_task not in task['tasklist']:
            new_task = {task_category:selected_task}
        else:
            random_index = randrange(0, len(task['tasklist']))
    else:
        new_task = {task_category:selected_task}
    return new_task


tasks = {
            'software':softwares,
            'electronics':electronics,
            'hardware':hardwares,
            'mac':macs,
            'maintainance':maintainances,
            'networking':networkings,
            'security':securities,
            'server':servers,
            'support':supports,
            'unix':unixs,
            'windows':windows
        }


def category_task(user_id):
    all_tasks = []
    for key,value in tasks.iteritems():
        task = assign_task(user_id, key, value)
        task['name'] = key
        all_tasks.append(task)
    return all_tasks
