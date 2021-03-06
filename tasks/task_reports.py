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
            lastsixmonths.insert(0,months[-i-1])
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
    for i in lst:
        if i.date_opened is not None :
            if i.category == task_category:
                months[datetime.strptime(str(i.date_opened), '%Y-%m-%d %H:%M:%S.%f').month-1] += 1
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


def get_closed_user_monthly_tasks(lst, task_category):
    months = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in lst:
        if i.date_resolved is not None:
            if i.category == task_category:
                months[datetime.strptime(str(i.date_resolved), '%Y-%m-%d %H:%M:%S.%f').month-1] += 1
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
    count = 0
    for i in lst:
        if i.date_resolved is not None:
            if i.category == category:
                count += 1
                if i.satisfaction is None:
                    months[datetime.strptime(str(i.date_resolved), '%Y-%m-%d %H:%M:%S.%f').month-1] += 0
                    months[datetime.strptime(str(i.date_resolved), '%Y-%m-%d %H:%M:%S.%f').month-1] = float(months[datetime.strptime(str(i.date_resolved), '%Y-%m-%d %H:%M:%S.%f').month-1])/2
                else:
                    months[datetime.strptime(str(i.date_resolved), '%Y-%m-%d %H:%M:%S.%f').month-1] += i.satisfaction
                    months[datetime.strptime(str(i.date_resolved), '%Y-%m-%d %H:%M:%S.%f').month-1] = float(months[datetime.strptime(str(i.date_resolved), '%Y-%m-%d %H:%M:%S.%f').month-1])/2
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
    task_categories = ["maintainance", "networking", "windows", "mac","support", "electronics", "server", "hardware", "unix", "security", "software"]
    avarage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for item in lst:
        if item.satisfaction is not None:
            for task in task_categories:
                if task == item.category:
                    avarage[task_categories.index(task)] += item.satisfaction
    return avarage


def get_user_avarage_time(closed_lst, opened_lst):
    task_categories = ["maintainance", "networking", "windows", "mac", "support", "electronics", "server", "hardware", "unix", "security", "software"]
    avarage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    count = 0
    for i in closed_lst:
        start = i.date_created
        end = i.date_opened
        start_dt = datetime.strptime(str(start), '%Y-%m-%d %H:%M:%S.%f')
        end_dt = datetime.strptime(str(end), '%Y-%m-%d %H:%M:%S.%f')
        diff = (end_dt - start_dt)
        total = diff.seconds/60 + diff.days*24*60
        total_hours = total
        if count == 0:
            avarage[task_categories.index(i.category)] += total_hours
        else:
            avarage[task_categories.index(i.category)] += total_hours
            avarage[task_categories.index(i.category)] = float(avarage[task_categories.index(i.category)]) / count
        count += 1

    for i in opened_lst:
        start = i.date_created
        end = i.date_opened
        start_dt = datetime.strptime(str(start), '%Y-%m-%d %H:%M:%S.%f')
        end_dt = datetime.strptime(str(end), '%Y-%m-%d %H:%M:%S.%f')
        diff = (end_dt - start_dt)
        total = diff.seconds/60 + diff.days*24*60
        total_hours = total
        if count == 0:
            avarage[task_categories.index(i.category)] += total_hours
        else:
            avarage[task_categories.index(i.category)] += total_hours
            avarage[task_categories.index(i.category)] = float(avarage[task_categories.index(i.category)]) / count
        count += 1

    return avarage


def get_user_avarage_time_closed(lst):
    task_categories = ["maintainance", "networking", "windows", "mac", "support", "electonics", "server", "hardware", "unix", "security"]
    avarage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    count = 0
    for i in lst:
        start = i.date_created
        end = i.date_resolved
        start_dt = datetime.strptime(str(start), '%Y-%m-%d %H:%M:%S.%f')
        end_dt = datetime.strptime(str(end), '%Y-%m-%d %H:%M:%S.%f')
        diff = (end_dt - start_dt)
        total = diff.seconds/60 + diff.days*24*60
        total_hours = total
        if count == 0:
            avarage[task_categories.index(i.category)] += total_hours
        else:
            avarage[task_categories.index(i.category)] += total_hours
            avarage[task_categories.index(i.category)] = float(avarage[task_categories.index(i.category)]) / count
        count += 1
    return avarage
