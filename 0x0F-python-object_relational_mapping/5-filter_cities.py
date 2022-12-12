#!/usr/bin/python3

"""Doc"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = db.cursor()
    cur.execute("""SELECT cities.name, states.name FROM cities
                JOIN states ON cities.state_id = states.id""")
    result = cur.fetchall()
    theCities = [rows[0] for rows in result if rows[1] == argv[4]]
    print(', '.join(theCities))
