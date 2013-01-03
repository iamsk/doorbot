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


class Borg():
    """
    base on http://blog.youxu.info/2010/04/29/borg
    - 单例配置收集类
    """
    __collective_mind = {}
    def __init__(self):
        self.__dict__ = self.__collective_mind

    def validate(self, username, password):
        dbdoorbot = "/home/pi/doorbot/doorbot.db"
        db = bdb.hashopen(dbdoorbot, 'c')
        password = hashlib.md5(password)
        return True if username in db and db[username] == password else False


borg = Borg()


@route('/door', method='POST')
def door():
    email = request.forms.get('email')
    password = request.forms.get('password')
    if borg.validate(email, password):
        print '%s login at  %s' % (email, datetime.now())
        open()
        return "Door opened!"
    else:
        return "Username/Password invalid!"


@route('/demo')
def demo():
    return 'Hello world!'


#run(host='127.0.0.1', port=9001, debug=False)
#run(host='0.0.0.0', port=9001, debug=False)
application = bottle.default_app()
httpserver.serve(application, host='127.0.0.1', port=9001)

