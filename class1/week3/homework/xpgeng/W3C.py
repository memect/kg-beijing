# -*- coding: utf-8 -*-

import json
import psycopg2

data = []
with open('W3C_data.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))
f.close()

conn.psycopg2.connect("dbname=W3C user=xpgeng")


for item in data:
