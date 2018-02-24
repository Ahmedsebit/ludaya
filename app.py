from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from ludaya.ludaya import app, db


from datetime import datetime
import time

from apscheduler.schedulers.background import BackgroundScheduler
from ludaya.users.user import user_blueprint
from ludaya.api.api_ludaya import api_blueprint
from tasks.usertask import allocate_all_user_tasks
app.register_blueprint(user_blueprint)
app.register_blueprint(api_blueprint)

def tick():
    print('Tick! The time is: %s' % datetime.now())


# if not app.debug or os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(allocate_all_user_tasks, 'interval', seconds=3)
#     scheduler.start()
#     print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

#     try:
#         # This is here to simulate application activity (which keeps the main thread alive).
#         while True:
#             time.sleep(2)
#     except (KeyboardInterrupt, SystemExit):
#         # Not strictly necessary if daemonic mode is enabled but should be done if possible
#         scheduler.shutdown()

# create_group()
# allocate_all_user_tasks()


if __name__ == '__main__':
    app.run() 