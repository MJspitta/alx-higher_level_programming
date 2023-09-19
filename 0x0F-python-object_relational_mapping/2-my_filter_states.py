#!/usr/bin/python3
"""displays all values in the states table where name matches argument
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    query_cmd = "SELECT * \
                    FROM states \
                    WHERE name LIKE '{:s}' ORDER BY id ASC".format(argv[4])
    cursor.execute(query_cmd)
    result = cursor.fetchall()
    for st in result:
        if st[1] == argv[4]:
            print(st)
    cursor.close()
    db.close()
