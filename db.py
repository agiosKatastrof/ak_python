#!/usr/bin/python

import mysql.connector

db = mysql.connector.connect(user='dad',password='k9Canine',host='10.0.0.8',db='bod')

cursor = db.cursor()

add = ("INSERT INTO Test (id,val) VALUES (%s, %s)")

val = (120,'Moid')

cursor.execute(add,val)

print cursor.lastrowid



db.commit()

get = ("SELECT id, val FROM Test ")

val2 = (120)

cursor.execute(get)

for (id,val) in cursor:
    print "%d %s" % (id,val)

get2 = ("SELECT val from Test WHERE id = '%s'")

cursor.execute(get2,val2)

for (val) in cursor:
    print "%s " % val
    
cursor.close()
db.close()