import bsddb as bdb
import hashlib


dbdoorbot = "/home/pi/doorbot/doorbot.db"
db = bdb.hashopen(dbdoorbot, 'c')
password = hashlib.md5('853211')
for key in db:
    if db[key] == password:
        del db[key]

