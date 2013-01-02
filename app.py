#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'iamsk'
__email__ = 'iamsk.info@gmail.com'

import sys,pickle
import time
import base64,hashlib
import subprocess
import bsddb as bdb

from bottle import route, run
from bottle import template

from door import open


class Borg():
    """
    base on http://blog.youxu.info/2010/04/29/borg
    - 单例配置收集类
    """
    __collective_mind = {}
    def __init__(self):
        self.__dict__ = self.__collective_mind

    dbdoorbot = "doorbot.db"
    db = bdb.hashopen(dbdoorbot, 'c')

    def validate(username, password):
        return True if db[username] == password else False


borg = Borg()


@route('/door')
def door(method='POST'):
    username = request.forms.get('username')
    password = request.forms.get('password')
    if borg.validate(username, password):
        #door.open()
        return "Door opened!"
    else:
        return "Username/Password invalid!"

run(host='0.0.0.0', port=8080, debug=True)

