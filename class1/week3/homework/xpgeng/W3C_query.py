# -*- coding: utf-8 -*-

import json
import psycopg2
import psycopg2.extras


conn = psycopg2.connect("dbname=W3C user=xpgeng")
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute('''SELECT data FROM W3C''')

row = cursor.fetchone()

dic = row['data']

print dic['headers']



cursor.close()
conn.close()