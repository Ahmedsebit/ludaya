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
