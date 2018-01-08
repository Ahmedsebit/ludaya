from taskallocations import AssignTasks
from flask_sqlalchemy import SQLAlchemy

from models import AssignedTask, User
from ludaya.ludaya import db
from datetime import datetime
assign_tasks = AssignTasks()

def allocate_all_user_tasks():
    communication = assign_tasks.communication_tasks()
    electronics = assign_tasks.electronics_task()
    hardware = assign_tasks.hardware_task()
    learning = assign_tasks.learning_task()
    mac = assign_tasks.mac_task()
    maintainance = assign_tasks.maintainance_task()
    networking = assign_tasks.networking_task()
    security = assign_tasks.security_task()
    server = assign_tasks.server_task()
    support = assign_tasks.support_task()
    unix = assign_tasks.unix_task()
    windows = assign_tasks.windows_task()

    users = User.query.all()

    for user in users:
        allocate(communication, user.id)
        allocate(electronics, user.id)
        allocate(hardware, user.id)
        allocate(learning, user.id)
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
