from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from ludaya.ludaya import app, db


from datetime import datetime
import time

from apscheduler.schedulers.background import BackgroundScheduler
from ludaya.users.user import user_blueprint 
from ludaya.api.api_ludaya import api_blueprint
# from tasks.usertask import allocate_all_user_tasks, async_allocate_all_user_tasks
from tasks.system_administrator.allocate_tasks import assign_system_admin_task
# from ludaya.users.groups import change_group_leader
app.register_blueprint(user_blueprint)
app.register_blueprint(api_blueprint)


# sched = BackgroundScheduler()
# # sched.add_job(tick,'interval',seconds=3)
# sched.start()

# @sched.scheduled_job('interval', seconds=10800)
# def daily_schedule():
#     # change_group_leader()
#     print("group leader changed")
#     # allocate_all_user_tasks()
#     print("tasks assigned")

assign_system_admin_task()
if __name__ == '__main__':
    app.run(use_reloader=False) 