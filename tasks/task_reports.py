import os


from flask_sqlalchemy import SQLAlchemy

from datetime import datetime


def last_six_months():
    currentMonth = datetime.now().month
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    lastsixmonths = []
    if currentMonth < 6:
        remainingmonths = 6 - currentMonth
        for i in range(0, remainingmonths):
            lastsixmonths.append(months[-i-1])
        for i in range(0, currentMonth):
            lastsixmonths.append(months[i])
    if currentMonth == 6:
        for i in range(0, currentMonth):
            lastsixmonths.append(months[i])
    if currentMonth > 6:
        lastmonths = currentMonth - 6
        for i in range(lastmonths, currentMonth):
            lastsixmonths.append(months[i])
    return lastsixmonths

def get_user_monthly_tasks(lst, task_category):
    months = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for month in months:
        for i in lst:
            if datetime.strptime(i.resolved_date, '%y-%m-%d %H:%M:%S.%f').month == months.index(month) and i.category == task_category:
                months[month] += 1
    lastsixmonths = []
    currentMonth = datetime.now().month
    if currentMonth < 6:
        remainingmonths = 6 - currentMonth
        for i in range(0, remainingmonths):
            lastsixmonths.append(months[-i-1])
        for i in range(0, currentMonth):
            lastsixmonths.append(months[i])
    if currentMonth == 6:
        for i in range(0, currentMonth):
            lastsixmonths.append(months[i])
    if currentMonth > 6:
        lastmonths = currentMonth - 6
        for i in range(lastmonths, currentMonth):
            lastsixmonths.append(months[i])
    return lastsixmonths



def get_user_monthly_satisfaction(lst, category):
    months = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for month in months:
        for i in lst:
            if datetime.strptime(i.resolved_date, '%y-%m-%d %H:%M:%S.%f').month == months.index(month) and i.category == category:
                months[month] += i.satisfaction
                months[month] = months[month]/2
    lastsixmonths = []
    currentMonth = datetime.now().month
    if currentMonth < 6:
        remainingmonths = 6 - currentMonth
        for i in range(0, remainingmonths):
            lastsixmonths.append(months[-i-1])
        for i in range(0, currentMonth):
            lastsixmonths.append(months[i])
    if currentMonth == 6:
        for i in range(0, currentMonth):
            lastsixmonths.append(months[i])
    if currentMonth > 6:
        lastmonths = currentMonth - 6
        for i in range(lastmonths, currentMonth):
            lastsixmonths.append(months[i])
    return lastsixmonths

def get_user_avarage_satisfaction(lst):
    task_categories = ["maintainance", "networking", "windows", "communication", "support", "electonics", "server", "hardware", "unix", "security"]
    avarage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in lst:
        for task in task_categories:
            if i.category == task_categories[task]:
                avarage[task] += i.date_ch
                avarage[task] = avarage[task] / 2
    return avarage

def get_user_avarage_time(lst, date_end):
    task_categories = ["maintainance", "networking", "windows", "communication", "support", "electonics", "server", "hardware", "unix", "security"]
    avarage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in lst:
        for task in task_categories:
            if i.category == task_categories[task]:
                start = i.date_resolved
                end = i.date_end
                start_dt = datetime.strptime(start, '%Y-%m-%d %H:%M:%S.%f')
                end_dt = datetime.strptime(end, '%Y-%m-%d %H:%M:%S.%f')
                diff = (end_dt - start_dt)
                avarage[task] += diff
                avarage[task] = avarage[task] / 2
    return avarage


def six_last_month_count():
    pass


def software_task(user_id):
    pass

def electronics_task(user_id):
    pass

def hardware_task(user_id):
    pass

def mac_task(user_id):
    pass

def maintainance_task(user_id):
    pass

def networking_task(user_id):
    pass

def security_task(user_id):
    pass

def server_task(user_id):
    pass

def support_task(user_id):
    pass

def unix_task(user_id):
    pass

def windows_task(user_id):
    pass

last_six_months()