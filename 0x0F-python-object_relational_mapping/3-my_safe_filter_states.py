#!/usr/bin/python3

"""Doc"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
    
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id""")
    result = cur.fethall()
    
    for rows in result:
        if (rows[1] == sys.argv[4]):
            print(rows)
