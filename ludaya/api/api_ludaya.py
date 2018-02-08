from flask import Flask, render_template, session, flash, request, redirect, url_for, flash, jsonify, \
                Blueprint, g, redirect, abort, current_app
from flask_sqlalchemy import SQLAlchemy
import json
import os
import re
import string
import random
import datetime as dt

from tasks.alltasks import communcation, electronics, hardware, mac, maintainance, networking, security, server, support, unix, windows
from flask_sqlalchemy import SQLAlchemy

from models import AssignedTask, User


def get_all_category(category):
    # if 'username' in session:
    #     username = session['username']
    #     id = session['id']
    completed_items = AssignedTask.query.filter_by(status="completed", category =category, user_id=id).all()
    opened_items = AssignedTask.query.filter_by(status="opened",  category =category, user_id=id).all()
    
    all = list_length(category)
    
    return jsonify({'completed':len(completed_items),
                    'opened':len(opened_items),
                    'all':len(all)}
                    )
    
def get_issues(id):
    if 'username' in session:
        username = session['username']
        id = session['id']
        items = AssignedTask.query.filter_by(status="not started", user_id=id).all()
        completed_items = AssignedTask.query.filter_by(status="completed", user_id=id).all()
        opened_items = AssignedTask.query.filter_by(status="opened", user_id=id).all()
        groups_list = []
        groups_list_opened = []
        for i in items:
            groups_list.append(i.category)
        groups = {x:groups_list.count(x) for x in groups_list}
        for i in opened_items:
            groups_list_opened.append(i.category)
        groups_opened = {x:groups_list_opened.count(x) for x in groups_list_opened}


        return jsonify({
                'items':items,
                'groups':groups,
                'opened':groups_opened
        })

def list_length(category):
    l = []
    for i in category:
        for j in i.values()[0]:
            l.append(j)

    return l