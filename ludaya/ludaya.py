from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask import Blueprint, request, session, g, redirect, url_for, abort, \
     render_template, flash, current_app

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result


@app.route('/')
def hello():
    return render_template('home.html')


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)