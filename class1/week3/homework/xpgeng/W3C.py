# -*- coding: utf-8 -*-

import json
import psycopg2
import psycopg2.extras

data = []
with open('W3C_data.json', 'r') as f:
    for line in f:
        data.append(json.loads(line, encoding='utf-8'))
f.close()

conn = psycopg2.connect("dbname=W3C user=xpgeng")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS
    W3C(id serial primary key, data jsonb);
    ''')

for item in data:
    cursor.execute('''
        INSERT INTO W3C (data) VALUES (%s);
        ''', [psycopg2.extras.Json(item)])

conn.commit()

cursor.close()
conn.close()




