from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from ludaya.ludaya import app, db
from tasks.usertask import allocate_all_user_tasks, testing

from apscheduler.schedulers.background import BackgroundScheduler
import logging


if not app.debug or os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
    scheduler = BackgroundScheduler()
    scheduler.add_job(testing, 'interval', seconds=5, start_date='2018-01-07 13:00')
    scheduler.start()

# logging.basicConfig()
# logging.getLogger('apscheduler').setLevel(logging.DEBUG)

if __name__ == '__main__':
    app.run()