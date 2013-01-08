#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'iamsk'
__email__ = 'iamsk.info@gmail.com'

import sys, pickle
import time
from datetime import datetime
import base64, hashlib
import subprocess
import bsddb as bdb
from paste import httpserver

import bottle
from bottle import route, run
from bottle import template
from bottle import request

from door import open
from logger import initlogger


class Borg():
    """
    base on http://blog.youxu.info/2010/04/29/borg
    - 单例配置收集类
    """
    __collective_mind = {}
    def __init__(self):
        self.__dict__ = self.__collective_mind
        dbdoorbot = "/home/pi/doorbot/doorbot.db"
        self.db = bdb.hashopen(dbdoorbot, 'c')

    def validate(self, username, password):
        password = hashlib.md5(password).hexdigest()
        return True if username in self.db and self.db[username] == password else False

    def change_password(self, username, new_password):
        new_password = hashlib.md5(new_password).hexdigest()
        self.db[username] = new_password
        self.db.sync()


borg = Borg()
logger = initlogger()


@route('/door', method='POST')
def door():
    email = request.forms.get('email')
    password = request.forms.get('password')
    if borg.validate(email, password):
        logger.info('%s logined in.' % email)
        open()
        return "Door opened!"
    else:
        return "Username/Password invalid!"


@route('/password')
def password():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Password Change</title>
</head>
<body>
<form action="/password_change" method="POST">
    <p>Email: <input type="text" name="email" /></p>
    <p>Old Password: <input type="text" name="old_password" /></p>
    <p>New Password: <input type="text" name="new_password" /></p>
    <input type="submit" value="Submit" />
</form>
</body>
</html>
"""


@route('/password_change', method='POST')
def password_change():
    email = request.forms.get('email')
    old_password = request.forms.get('old_password')
    new_password = request.forms.get('new_password')
    if borg.validate(email, old_password):
        borg.change_password(email, new_password)
        return 'Changed success!'
    else:
        return "Username/Password invalid!"


#run(host='127.0.0.1', port=9001, debug=False)
#run(host='0.0.0.0', port=9001, debug=False)
application = bottle.default_app()
httpserver.serve(application, host='127.0.0.1', port=9001)

