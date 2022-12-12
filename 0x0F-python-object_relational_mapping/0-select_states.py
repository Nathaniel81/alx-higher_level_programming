import MySQLdb
import sys

if __name__ == "__main__":
	db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
	cursor = db.cursor()
	cursor.execute("SELECT * FROM states ORDER BY id")
	result = cursor.fetchall()
	
	for rows in result:
	    print(rows)