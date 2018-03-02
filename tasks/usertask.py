# coding: utf8

from flask_sqlalchemy import SQLAlchemy
from decorators import async
from models import AssignedTask, User, Groups
from ludaya.ludaya import db
from datetime import datetime
from tasksallocations import category_task
from notifications.slack import send_channel_messages, send_dm

def allocate_all_user_tasks():
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
                allocate(task, user.id, user.email)

        task_strng = ""
        # tasks_in_string =",".join(str(x) for x in tasks)

        for i in tasks:
            task_strng +=str(i)

        if len(tasks) > 0:
            message = ' *'+'New Task'+'*\n'+'```'+'Asigned to:'+user.firstname.lower().title()+' '+ user.lastname.lower().title() +'\n'+task_strng+'```'
            send_channel_messages(group.name, message)


def allocate(task, user, email):
    category = task['name']
    group = task.keys()[0]
    name = task[group]
    if category != name:
        new_task = AssignedTask(name=name, group=group, category=category, user_id=user)
        db.session.add(new_task)
        db.session.commit()


def get_user_tasks(user_id):
    tasks = AssignedTask.get_assignedtask(user_id)
    lst = []
    for task in tasks:
        lst.append(task)
    return lst
