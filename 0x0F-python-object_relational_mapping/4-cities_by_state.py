#!/usr/bin/python3

"""Doc"""

import MySQLdb
from sys import argv

db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
        )
cur = db.cursor()
cur.execute("SELECT cities.id, cities.name, states.name from cities
        JOIN states ON cities.state_id = states.id")
result = cur.fetchall()

for rows in result:
    print(rows)
