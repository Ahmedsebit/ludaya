from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from ludaya.ludaya import app, db


from datetime import datetime
import time

from apscheduler.schedulers.background import BackgroundScheduler
from .ludaya.users.user import user_blueprint
from ludaya.api.api_ludaya import api_blueprint
from tasks.usertask import allocate_all_user_tasks, async_allocate_all_user_tasks
app.register_blueprint(user_blueprint)
app.register_blueprint(api_blueprint)


# sched = BackgroundScheduler()
# # sched.add_job(tick,'interval',seconds=3)
# sched.start()

# @sched.scheduled_job('interval', seconds=3)
# def tick2():
#     sensor()

# try:
#     app
# except (KeyboardInterrupt, SystemExit):
#     sched.shutdown()

# create_group()
# allocate_all_user_tasks()
# async_allocate_all_user_tasks()


if __name__ == '__main__':
    app.run(use_reloader=False) 