import os
from datetime import datetime
from models import AssignedTask, User, MonthlyData
from ludaya.ludaya import db
from notifications.mail import send_mail
from tasks.mail import notify, format_email
from tasks.review_actions import send_weekly_data, send_monthly_data, save_monthly_data, perfomance_review


def weekly_review():
    users = User.query.all()
    for user in users:
        send_weekly_data(user.id)


def monthly_review():
    users = User.query.all()
    for user in users:
        send_monthly_data(user.id)
        save_monthly_data(user.id)
        # perfomance_review(user.id)
        
            
