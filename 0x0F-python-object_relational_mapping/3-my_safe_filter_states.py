#!/usr/bin/python3
"""display all values in the states table where name matched the argument
but this time it should be safe from MySQL injections
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    query_cmd = """SELECT * \
                    FROM states \
                    WHERE name=%s ORDER BY id ASC"""
    cursor.execute(query_cmd, (argv[4],))
    result = cursor.fetchall()
    for st in result:
        print(st)
    cursor.close()
    db.close()
