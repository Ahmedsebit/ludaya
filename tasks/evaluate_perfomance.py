import os
from datetime import datetime
from models import AssignedTask, User, MonthlyData
from ludaya.ludaya import db
from notifications.mail import send_mail


def get_monthly_avarage_perfomance_time(task_lst):
    timeseries = []
    for i in task_lst:
        if i.date_resolved:
            while datetime.strptime(str(i.date_resolved), '%Y-%m-%d %H:%M:%S.%f').month == datetime.now().month:
                start = i.date_created
                end = i.date_resolved
                start_dt = datetime.strptime(str(start), '%Y-%m-%d %H:%M:%S.%f')
                end_dt = datetime.strptime(str(end), '%Y-%m-%d %H:%M:%S.%f')
                diff = (end_dt - start_dt)
                total = diff.seconds/60 + diff.days*24*60
                timeseries.append(total)
    avaragetime = 0
    if len(timeseries)>0:
        avaragetime = sum(timeseries)/len(timeseries)
    return avaragetime


def get_weekly_avarage_perfomance_time(task_lst):
    timeseries = []
    for i in task_lst:
        if i.date_resolved:
            task_date = datetime.strptime(str(i.date_resolved), '%Y-%m-%d %H:%M:%S.%f')
            while task_date.day > datetime.now().day-5 and task_date.day < datetime.now().day+1:
                start = i.date_created
                end = i.date_resolved
                start_dt = datetime.strptime(str(start), '%Y-%m-%d %H:%M:%S.%f')
                end_dt = datetime.strptime(str(end), '%Y-%m-%d %H:%M:%S.%f')
                diff = (end_dt - start_dt)
                total = diff.seconds/60 + diff.days*24*60
                timeseries.append(total)
    avaragetime = 0
    if len(timeseries)>0:
        avaragetime = sum(timeseries)/len(timeseries)
    return avaragetime


def get_weekly_avarage_quality(task_lst):
    weekly_resolved = []
    weekly_all_tasks = []
    avarage_quality = 0
    completion_rate = 0
    for i in task_lst:
        if i.date_resolved:
            task_date = datetime.strptime(str(i.date_resolved), '%Y-%m-%d %H:%M:%S.%f')
            while task_date.day > datetime.now().day-5 and task_date.day < datetime.now().day+1:
                if i.date_resolved:
                    weekly_resolved.append(i.satisfaction)
                if i.date_opened:
                    weekly_all_tasks.append(i)
    if len(weekly_resolved)>0:
        avarage_quality = sum(weekly_resolved)/len(weekly_resolved)
    if len(weekly_resolved) !=0 or len(weekly_all_tasks) !=0:
        completion_rate = sum(weekly_resolved)/sum(weekly_all_tasks)
    weekly_quality_data = {
                            'avarage_quality':avarage_quality,
                            'completion_rate':completion_rate    
                            }
    return weekly_quality_data


def get_monthly_avarage_quality(task_lst):
    month_resolved = []
    month_all_tasks = []
    avarage_quality = 0
    completion_rate = 0
    for i in task_lst:
        if i.date_resolved:
            while datetime.strptime(str(i.date_resolved), '%Y-%m-%d %H:%M:%S.%f').month == datetime.now().month:
                if i.date_resolved:
                    if i.satisfaction is None:
                        month_resolved.append(0)
                    else:
                        month_resolved.append(i.satisfaction)
                if i.date_opened:
                    month_all_tasks.append(i)
    if len(month_resolved)>0:
        avarage_quality = sum(month_resolved)/len(month_resolved)
    if len(month_resolved) !=0 or len(month_all_tasks) !=0:
        completion_rate = sum(month_resolved)/sum(month_all_tasks)
    weekly_quality_data = {
                            'avarage_quality':avarage_quality,
                            'completion_rate':completion_rate    
                            }
    return weekly_quality_data


# from tasks.review_actions import deactivate_user, send_warning, send_deactivate
# def monthly_review_capture(user_id, email):
#     task_lst = AssignedTask.query.filter_by(user_id=user_id).all()
#     user = User.query.filter_by(id=user_id).first()
#     time = get_weekly_avarage_perfomance_time(task_lst)
#     quality = get_weekly_avarage_quality(task_lst)    
#     if time > 100 or quality['avarage_quaity'] <0.2 or quality['completion_rate']<0.3:
#         if user.warning < 3:
#             send_warning(user.warning, email, time, quality)
#             user.warnings += 1 
#             db.session.add(user)
#             db.session.commit()
#         elif user.warning > 2:
#             deactivate_user(user.id)
#             send_deactivate(email, time, quality)
#         elif user.warning is None:
#             send_warning(user.warning, email, time, quality)
#             user.warnings = 1 
#             db.session.add(user)
#             db.session.commit()
