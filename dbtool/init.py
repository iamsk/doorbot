import bsddb as bdb
import csv
import hashlib


dbdoorbot = "/home/pi/doorbot/doorbot.db"
db = bdb.hashopen(dbdoorbot, 'c')
password = hashlib.md5('853211')
reader = csv.reader(open("init.csv"))
for email in reader:
    db[email] = password

