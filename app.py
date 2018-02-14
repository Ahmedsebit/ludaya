from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from ludaya.ludaya import app, db
from tasks.usertask import allocate_all_user_tasks, testing, get_user_tasks
from tasks.tasksallocations import get_user_assigned_tasks

from apscheduler.schedulers.background import BackgroundScheduler
from tasks.communications import COMMUNICATION

if not app.debug or os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
    scheduler = BackgroundScheduler()
    scheduler.add_job(testing, 'interval', seconds=5, start_date='2018-01-07 13:00')
    scheduler.start()


# allocate_all_user_tasks()
if __name__ == '__main__':
    app.run()