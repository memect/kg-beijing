# -*- coding: utf-8 -*-

import psycopg2

conn = psycopg2.connect(database='test_db', host='localhost', port='5432',
                    user='postgres', password='1001')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS
    dish(name text, data jsonb)
    ''')
conn.commit()