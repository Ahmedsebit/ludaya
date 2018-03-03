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
from ludaya.ludaya import app
from decorators import async
from datetime import datetime, time

db = SQLAlchemy(app)

from models import User, Groups, AssignedTask, assignedtask_schema, assignedtasks_schema
from notifications.slack import create_channel


def create_group(team_lead):
    lastgroup = get_last_created_group()
    if lastgroup:
        name = 'LUDAYA_TESTING'+str(lastgroup.id)
        group = Groups(name=name, current_members=1, team_lead=team_lead)
        db.session.add(group)
        db.session.commit()
        db.session.refresh(group)
        # create_channel(name)
        return group
    else:
        name = 'LUDAYA_TESTING'
        group = Groups(name=name, current_members=1, team_lead=team_lead)
        db.session.add(group)
        db.session.commit()
        db.session.refresh(group)
        # create_channel(name)
        return group


def get_last_created_group():
    lastgroup = Groups.query.order_by('-id').first()
    return lastgroup


@async
def async_change_group_leader(group_id):
    group_users = User.query.filter_by(group=group_id).all()
    group = Groups.query.filter_by(id=group_id).first()
    for user in group_users:
        if group.team_lead == user.id:
            if group_users.index(user)+1==len(group_users):
                group.team_lead = group_users[0].id
                group.save()
                break
            else:
                group.team_lead = group_users[group_users.index(user)+1].id
                group.save()
                break


def change_group_leader():
    now = datetime.now()
    now_time = now.time()
    if now_time >= time(10,30) and now_time <= time(15,30):
        groups = Groups.query.all()
        for group in groups:
            async_change_group_leader(group.id)
