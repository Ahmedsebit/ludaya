import os

from communications import COMMUNICATION as communications
from electronics import ELECTRONICS as electronics
from hardware import HARDWARE as hardwares
from learning import LEARNING as learnings
from mac import MAC as macs
from maintainance import MAINTAINANCE as maintainances
from networking import NETWORKING as networkings
from security import SECURITY as securities
from server import SERVER as servers
from support import SUPPORT as supports
from unix import UNIX as unixs
from windows import WINDOWS as windows
from users.user import Communication, Electronics, Hardware, Learning, Mac, Maintainance, Networking, Security, Server, Support, Unix, Windows

from random import randrange


class AssignTasks(object):

    def __init__(self):
        self.commnunication_list = []
        self.electronics_list = []
        self.hardware_list = []
        self.learning_list = []
        self.mac_list = []
        self.maintainance_list = []
        self.networking_list = []
        self.security_list = []
        self.server_list = []
        self.support_list = []
        self.unix_list = []
        self.windows_list = []

    def assign_task(self, category, category_list):
        main_random_index = randrange(0, len(category))
        task = category[main_random_index]
        task_category = task['name']
        random_index = randrange(0, len(task['tasklist']))
        selected_task = task['tasklist'][random_index]
        new_task = {task_category:selected_task}
        if len(category_list) > 0:
            for k in category_list:
                if k['name'] == task_category:
                    if new_task in k['tasklist']:
                        random_index = randrange(0, len(task['tasklist']))
                        selected_task = task['tasklist'][random_index]
                        new_task = {task_category:selected_task}
                    k['tasklist'].append(selected_task)
                else:
                    category_list.append({'name':task_category, 'tasklist':[selected_task]})
        else:
            category_list.append({'name':task_category, 'tasklist':[selected_task]})
        return new_task

    def communication_tasks(self):
        task = self.assign_task(communications, self.commnunication_list)
        task['name'] = 'communication'
        return task

    def electronics_task(self):
        task = self.assign_task(electronics, self.electronics_list)
        task['name'] = 'electonics'
        return task

    def hardware_task(self):
        task = self.assign_task(hardwares, self.hardware_list)
        task['name'] = 'hardware'
        return task

    def learning_task(self):
        task = self.assign_task(learnings, self.learning_list)
        task['name'] = 'learning'
        return task

    def mac_task(self):
        task = self.assign_task(macs, self.mac_list)
        task['name'] = 'mac'
        return task

    def maintainance_task(self):
        task = self.assign_task(maintainances, self.maintainance_list)
        task['name'] = 'maintainance'
        return task

    def networking_task(self):
        task = self.assign_task(networkings, self.networking_list)
        task['name'] = 'networking'
        return task

    def security_task(self):
        task = self.assign_task(securities, self.security_list)
        task['name'] = 'security'
        return task

    def server_task(self):
        task = self.assign_task(servers, self.server_list)
        task['name'] = 'server'
        return task

    def support_task(self):
        task = self.assign_task(supports, self.support_list)
        task['name'] = 'support'
        return task

    def unix_task(self):
        task = self.assign_task(unixs, self.unix_list)
        task['name'] = 'unix'
        return task

    def windows_task(self):
        task = self.assign_task(windows, self.windows_list)
        task['name'] = 'windows'
        return task
