import bsddb as bdb
import hashlib


dbdoorbot = "/home/pi/doorbot/doorbot.db"
db = bdb.hashopen(dbdoorbot, 'c')
count = 0
for key in db:
    print key
    count += 1
print count

