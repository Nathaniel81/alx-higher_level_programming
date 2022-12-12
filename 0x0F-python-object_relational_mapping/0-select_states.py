import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cursor = db.cursor()
cursor.execute(SELECT states.id, states.name FROM states; ORDER BY states.id)
result = cursor.fetchall()

for rows in result:
    print(rows)
