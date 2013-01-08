import bsddb as bdb
import hashlib


dbdoorbot = "/home/pi/doorbot/doorbot.db"
db = bdb.hashopen(dbdoorbot, 'c')
count = 0
for k, v in db.items():
    print k, v
    count += 1
print count

