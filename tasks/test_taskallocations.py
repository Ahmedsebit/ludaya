from alltasks import ALLTASKS
import unittest
import os

from flask import Flask, render_template, session, flash, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
import re
from flask import Blueprint, request, session, g, redirect, url_for, abort, \
     render_template, flash, current_app
from validate_email import validate_email
from flask_bootstrap import Bootstrap

from ludaya.ludaya import app, db
from taskallocations import AssignTasks

from software import SOFTWARE as software
from electronics import ELECTRONICS as electronics
from hardware import HARDWARE as hardware
from learning import LEARNING as learning
from mac import MAC as mac
from maintainance import MAINTAINANCE as maintainance
from networking import NETWORKING as networking
from security import SECURITY as security
from server import SERVER as server
from support import SUPPORT as support
from unix import UNIX as unix
from windows import WINDOWS as windows

class LudayaTestCase(unittest.TestCase):
    '''
    This class represents the ludaya test case
    '''

    def setUp(self):
        '''
        Define test variables and initialize app.
        '''
        self.assign_tasks = AssignTasks()

    def test_asign_task(self):
        pass

    def test_software_task(self):
        items = []
        for i in software:
            items += i['tasklist']
        dic = self.assign_tasks.software_tasks()
        self.assertIn(dic.values()[0], items)

    def test_electronics_task(self):
        items = []
        for i in electronics:
            items += i['tasklist']
        dic = self.assign_tasks.electronics_task()
        self.assertIn(dic.values()[0], items)

    def test_hardware_task(self):
        items = []
        for i in hardware:
            items += i['tasklist']
        dic = self.assign_tasks.hardware_task()
        self.assertIn(dic.values()[0], items)

    def test_learning_task(self):
        items = []
        for i in learning:
            items += i['tasklist']
        dic = self.assign_tasks.learning_task()
        self.assertIn(dic.values()[0], items)

    def test_mac_task(self):
        items = []
        for i in mac:
            items += i['tasklist']
        dic = self.assign_tasks.mac_task()
        self.assertIn(dic.values()[0], items)

    def test_maintainance_task(self):
        items = []
        for i in maintainance:
            items += i['tasklist']
        dic = self.assign_tasks.maintainance_task()
        self.assertIn(dic.values()[0], items)

    def test_networking_task(self):
        items = []
        for i in networking:
            items += i['tasklist']
        dic = self.assign_tasks.networking_task()
        self.assertIn(dic.values()[0], items)

    def test_security_task(self):
        items = []
        for i in security:
            items += i['tasklist']
        dic = self.assign_tasks.security_task()
        self.assertIn(dic.values()[0], items)

    def test_server_task(self):
        items = []
        for i in server:
            items += i['tasklist']
        dic = self.assign_tasks.server_task()
        self.assertIn(dic.values()[0], items)

    def test_support_task(self):
        items = []
        for i in support:
            items += i['tasklist']
        dic = self.assign_tasks.support_task()
        self.assertIn(dic.values()[0], items)

    def test_unix_task(self):
        items = []
        for i in unix:
            items += i['tasklist']
        dic = self.assign_tasks.unix_task()
        self.assertIn(dic.values()[0], items)

    def test_windows_task(self):
        items = []
        for i in windows:
            items += i['tasklist']
        dic = self.assign_tasks.windows_task()
        self.assertIn(dic.values()[0], items)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
