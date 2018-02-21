from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from ludaya.ludaya import app, db

from apscheduler.schedulers.background import BackgroundScheduler
from ludaya.users.user import user_blueprint
from ludaya.api.api_ludaya import api_blueprint
# from users.groups import create_group

app.register_blueprint(user_blueprint)
app.register_blueprint(api_blueprint)
# if not app.debug or os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(testing, 'interval', seconds=5, start_date='2018-01-07 13:00')
#     scheduler.start()

# create_group()
# allocate_all_user_tasks()
if __name__ == '__main__':
    app.run() 