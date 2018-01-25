from taskallocations import AssignTasks
from flask_sqlalchemy import SQLAlchemy

from models import AssignedTask, User
from ludaya.ludaya import db
from datetime import datetime
from tasksallocations import electronics_task, hardware_task, learning_task, mac_task, maintainance_task, networking_task, security_task, server_task, software_task, support_task, unix_task, windows_task

def allocate_all_user_tasks():

    users = User.query.all()

    for user in users:
        electronics = electronics_task(user.id)
        hardware = hardware_task(user.id)
        learning = learning_task(user.id)
        mac = mac_task(user.id)
        maintainance = maintainance_task(user.id)
        networking = networking_task(user.id)
        security = security_task(user.id)
        server = server_task(user.id)
        support = support_task(user.id)
        software = software_task(user.id)
        unix = unix_task(user.id)
        windows = windows_task(user.id)

        allocate(software, user.id)
        allocate(electronics, user.id)
        allocate(hardware, user.id)
        allocate(learning, user.id)
        allocate(mac, user.id)
        allocate(maintainance, user.id)
        allocate(networking, user.id)
        allocate(security, user.id)
        allocate(server, user.id)
        allocate(support, user.id)
        allocate(unix, user.id)
        allocate(windows, user.id)

def allocate(task, user):
    category = task['name']
    group = task.keys()[0]
    name = task[group]

    new_task = AssignedTask(name=name, group=group, category=category, user_id=user)
    db.session.add(new_task)
    db.session.commit()

def testing():
    print('Hello Job! The time is: %s' % datetime.now())

def get_user_tasks(user_id):
    tasks = AssignedTask.get_assignedtask(user_id)
    lst = []
    for task in tasks:
        lst.append(task)
    return lst
