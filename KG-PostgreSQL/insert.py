#!/usr/bin/env python3

import psycopg2

conn = psycopg2.connect(
    database='food_db',
    host='localhost',
    port='5432',
    user='postgres',
    password='newpass')

cursor = conn.cursor()

import json

dish = json.load(open('dish.json', 'r'))
stuff = json.load(open('stuff.json', 'r'))

for i in dish:
    name = i['名称']
    cursor.execute('''
    INSERT INTO dish VALUES
    (%s, %s)
    ''', [name, json.dumps(i)])

for i in stuff:
    name = i['名称']
    cursor.execute('''
    INSERT INTO stuff VALUES
    (%s, %s)
    ''', [name, json.dumps(i)])

conn.commit() # 插入、修改时务必

cursor.close()
conn.close()

print('成功')
