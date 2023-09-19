#!/usr/bin/python3
"""script that lists all states with name starting with N from database
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    result = cursor.fetchall()
    for row in result:
        if row[1][0] == "N":
            print(row)
    cursor.close()
    db.close()
