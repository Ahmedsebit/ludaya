from flask_sqlalchemy import SQLAlchemy
from decorators import async
from models import AssignedTask, User, Groups
from ludaya.ludaya import db
from datetime import datetime
from tasksallocations import category_task

def allocate_all_user_tasks():
    async_allocate_all_user_tasks()

@async
def async_allocate_all_user_tasks():
    users = User.query.all()
    for user in users:
        group = Groups.query.filter_by(id = user.group).first()
        all_tasks = category_task(user.id)
        for task in all_tasks:
            if group.team_lead != user.id:
                allocate(task, user.id)

def allocate(task, user):
    category = task['name']
    group = task.keys()[0]
    name = task[group]
    new_task = AssignedTask(name=name, group=group, category=category, user_id=user)
    db.session.add(new_task)
    db.session.commit()


def get_user_tasks(user_id):
    tasks = AssignedTask.get_assignedtask(user_id)
    lst = []
    for task in tasks:
        lst.append(task)
    return lst
