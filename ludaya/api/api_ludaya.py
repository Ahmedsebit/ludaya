# from flask import Flask, render_template, session, flash, request, redirect, url_for, flash, jsonify
# from flask_sqlalchemy import SQLAlchemy
# import os
# import re
# import datetime as dt
# from flask import Blueprint, request, session, g, redirect, url_for, abort, \
#      render_template, flash, current_app

# from ludaya.ludaya import app

# tasks = [
#     {
#         'id': 1,
#         'title': u'Buy groceries',
#         'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
#         'done': False
#     },
#     {
#         'id': 2,
#         'title': u'Learn Python',
#         'description': u'Need to find a good Python tutorial on the web', 
#         'done': False
#     }
# ]

# @app.route('/todo/api/v1.0/tasks', methods=['GET'])
# def get_tasks():
#     return jsonify({'tasks': tasks})