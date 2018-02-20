from flask import Flask, render_template, session, flash, request, redirect, url_for, flash, jsonify, \
                Blueprint, g, redirect, abort, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import json
import os
import re
import string
import random
import math
import datetime as dt
from validate_email import validate_email
from flask_bootstrap import Bootstrap
from tasks.alltasks import communcation_list_length, electronics_list_length, hardware_list_length, learning_list_length, mac_list_length, maintainance_list_length, networking_list_length, security_list_length, server_list_length, support_list_length, unix_list_length, windows_list_length
from tasks.alltasks import communication, electronics, hardware, mac, maintainance, networking, security, server, support, unix, windows
from tasks.task_reports import last_six_months, get_user_monthly_tasks, get_user_monthly_satisfaction, get_user_avarage_time, get_user_avarage_satisfaction, get_closed_user_monthly_tasks, get_user_avarage_time_closed

from flask_marshmallow import Marshmallow

app = Flask(__name__)
Bootstrap(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
ma = Marshmallow(app)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ahmedamedy@gmail.com'
app.config['MAIL_PASSWORD'] = 'osmantito88'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

db = SQLAlchemy(app)

from models import User, Groups, AssignedTask, assignedtask_schema, assignedtasks_schema


def create_group(team_lead):
    lastgroup = get_last_created_group()
    name = 'LUDAYATESTING'+str(lastgroup.id)
    group = Groups(name=name, current_members=1, team_lead=team_lead)
    db.session.add(group)
    db.session.commit()
    db.session.refresh(group)
    return group

def get_last_created_group():
    lastgroup = Groups.query.order_by('-id').first()
    return lastgroup