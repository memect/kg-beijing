# -*- coding: utf-8 -*-

import json
import psycopg2

conn = psycopg2.connect(database='test_db', host='localhost', port='5432',
                    user='postgres', password='1001')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS
    dish(name text, data jsonb)
    ''')

cursor.execute('''
    INSERT INTO dish
    VALUES (%s, %s)
    ''', ['仰望星空', '{"人数": 2, "时间": "30分钟"}'])


cursor.execute('''
    SELECT '{"名称": "仰望星空"}'::jsonb
    ||'{"口味": {"奇葩": "满分"}}'::jsonb''')


cursor.execute('''
    SELECT name, data
    FROM dish
    ''',)

for item in cursor.fetchone():
    print item
conn.commit()
