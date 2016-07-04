#!/usr/bin/env python3

import psycopg2

conn = psycopg2.connect(
    database='food_db',
    host='localhost',
    port='5432',
    user='postgres',
    password='newpass')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS
dish (name text, data jsonb)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS
stuff (name text, data jsonb)
''')

conn.commit() # 插入、修改时务必

cursor.close()
conn.close()

print('成功')
