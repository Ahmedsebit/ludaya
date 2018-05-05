import os
from datetime import datetime
from models import AssignedTask, User, MonthlyData
from ludaya.ludaya import db
from notifications.mail import send_mail
from tasks.evaluate_perfomance import get_monthly_avarage_perfomance_time, get_monthly_avarage_quality, get_weekly_avarage_perfomance_time, get_weekly_avarage_quality
from tasks.mail import notify, format_email
from tasks.messages import first_warning, second_warning, third_warning, dismissal
from tasks.mail import notify, format_email


def save_monthly_data(user_id):
    task_lst = AssignedTask.query.filter_by(user_id=user_id).all()
    time = get_monthly_avarage_perfomance_time(task_lst)
    quality = get_monthly_avarage_quality(task_lst)
    new_task = MonthlyData(
        avarage_time=time, 
        avarage_quality=quality['avarage_quality'], 
        completion_rate=quality['completion_rate'], 
        user_id=user_id)
    db.session.add(new_task)
    db.session.commit()


def send_weekly_data(user_id):
    task_lst = AssignedTask.query.filter_by(user_id=user_id).all()
    user = User.query.filter_by(id=user_id).first()
    time = get_weekly_avarage_perfomance_time(task_lst)
    quality = get_weekly_avarage_quality(task_lst)
    message = []
    report_message = 'This is your weekly report:' + '\n'
    message.append('Avarage task completion time: ' + str(time) + '\n')
    message.append('Avarage task quality: ' + str(quality['avarage_quality']) + '\n')
    message.append('Completion rate: ' + str(quality['completion_rate']) + '\n')
    report_heading = 'Weekly report'
    tasks = format_email(message, report_message)
    notify(report_heading, user.email, tasks)


def send_monthly_data(user_id):
    task_lst = AssignedTask.query.filter_by(user_id=user_id).all()
    user = User.query.filter_by(id=user_id).first()
    time = get_monthly_avarage_perfomance_time(task_lst)
    quality = get_monthly_avarage_quality(task_lst)
    message = []
    report_message = 'This is your monthly report:' + '\n'
    message.append('Avarage task completion time: ' + str(time) + '\n')
    message.append('Avarage task quality: ' + str(quality['avarage_quality'])  + '\n')
    message.append('Completion rate: ' + str(quality['completion_rate']) + '\n')
    report_heading = 'Monthly report'
    tasks = format_email(message, report_message)
    notify(report_heading, user.email, tasks)


def send_warning(user_warning, email, time, quality):
    message = []
    report_heading = 'Perfomance Warning'
    if user_warning == 1:
        report_message = first_warning + '\n'
        message.append('Avarage task completion time: ' + str(time) + '\n')
        message.append('Avarage task quality: ' + str(quality['avarage_quality']) + '\n')
        message.append('Completion rate: ' + str(quality['completion_rate']) + '\n')
    elif user_warning == 2:
        report_message = second_warning + '\n'
        message.append('Avarage task completion time: ' + str(time) + '\n')
        message.append('Avarage task quality: ' + str(quality['avarage_quality']) + '\n')
        message.append('Completion rate: ' + str(quality['completion_rate']) + '\n')
    elif user_warning == 3:
        report_message = third_warning + '\n'
        message.append('Avarage task completion time: ' + str(time) + '\n')
        message.append('Avarage task quality: ' + str(quality['avarage_quality']) + '\n')
        message.append('Completion rate: ' + str(quality['completion_rate']) + '\n')
    tasks = format_email(message, report_message)
    notify(report_heading, email, tasks)


def send_deactivate(email, time, quality):
    message = []
    report_message = dismissal + '\n'
    message.append('Avarage task completion time: ' + str(time) + '\n')
    message.append('Avarage task quality: ' + str(quality['avarage_quality']))
    message.append('Completion rate: ' + str(quality['completion_rate']) + '\n')
    report_heading = 'Account Deactivated'
    tasks = format_email(message, report_message)
    notify(report_heading, email, tasks)


def deactivate_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        user.status = 'Deactivated' 
        db.session.add(user)
        db.session.commit()

def perfomance_review(user_id):
    task_lst = AssignedTask.query.filter_by(user_id=user_id).all()
    time = get_weekly_avarage_perfomance_time(task_lst)
    quality = get_weekly_avarage_quality(task_lst)    
    if time > 100 or quality['avarage_quality'] <0.2 or quality['completion_rate']<0.3:
        user = User.query.filter_by(id=user_id).first()
        if user.warning is None:
            user.warnings = 1 
            db.session.add(user)
            db.session.commit()
            send_warning(user.warning, user.email, time, quality)
        elif user.warning < 3:
            user.warnings += 1 
            db.session.add(user)
            db.session.commit()
            send_warning(user.warning, user.email, time, quality)
        elif user.warning > 2:
            deactivate_user(user.id)