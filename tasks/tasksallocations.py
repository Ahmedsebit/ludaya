import os


from flask_sqlalchemy import SQLAlchemy

from models import AssignedTask, User
from ludaya.ludaya import db

from software import SOFTWARE as softwares
from electronics import ELECTRONICS as electronics
from hardware import HARDWARE as hardwares
from learning import LEARNING as learnings
from mac import MAC as macs
from maintainance import MAINTAINANCE as maintainances
from networking import NETWORKING as networkings
from security import SECURITY as securities
from server import SERVER as servers
from support import SUPPORT as supports
from unix import UNIX as unixs
from windows import WINDOWS as windows
from users.user import Communication, Electronics, Hardware, Learning, Mac, Maintainance, Networking, Security, Server, Support, Unix, Windows

from random import randrange


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

def software_tasks(user_id):
    task = assign_task(user_id, 'software', softwares)
    task['name'] = 'software'
    return task

def electronics_task(user_id):
    task = assign_task(user_id, 'electronics', electronics)
    task['name'] = 'electonics'
    return task

def hardware_task(user_id):
    task = assign_task(user_id, 'hardware', hardwares)
    task['name'] = 'hardware'
    return task

def learning_task(user_id):
    task = assign_task(user_id, 'learning', learnings)
    task['name'] = 'learning'
    return task

def mac_task(user_id):
    task = assign_task(user_id, 'mac', macs)
    task['name'] = 'mac'
    return task

def maintainance_task(user_id):
    task = assign_task(user_id, 'maintainance', maintainances)
    task['name'] = 'maintainance'
    return task

def networking_task(user_id):
    task = assign_task(user_id, 'networking', networkings)
    task['name'] = 'networking'
    return task

def security_task(user_id):
    task = assign_task(user_id, 'security', securities)
    task['name'] = 'security'
    return task

def server_task(user_id):
    task = assign_task(user_id, 'server', servers)
    task['name'] = 'server'
    return task

def support_task(user_id):
    task = assign_task(user_id, 'support', supports)
    task['name'] = 'support'
    return task

def unix_task(user_id):
    task = assign_task(user_id, 'unix', unixs)
    task['name'] = 'unix'
    return task

def windows_task(user_id):
    task = assign_task(user_id, 'windows', windows)
    task['name'] = 'windows'
    return task
