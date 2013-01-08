import bsddb as bdb
import hashlib


dbdoorbot = "/home/pi/doorbot/doorbot.db"
db = bdb.hashopen(dbdoorbot, 'c')
password = hashlib.md5('853211').hexdigest()
del_list = []
for key in db:
    if db[key] == password:
        del_list.append(key)

count = 0
for k in del_list:
    print k
    count += 1
    #del db[k]
print count

