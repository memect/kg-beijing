# -*- coding: utf-8 -*-

import json
import psycopg2
import psycopg2.extras


conn = psycopg2.connect("dbname=W3C user=xpgeng")
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# query headers->From = Bobby Tung <bobbytung@wanderer.tw>
cursor.execute('''SELECT data FROM W3C 
    WHERE data #> '{headers, From}' = '"Bobby Tung <bobbytung@wanderer.tw>"' ''')

row = cursor.fetchone()

print row

cursor.close()
conn.close()