#!/usr/bin/python3
"""script that takes in an argument and displays
all values in the states table of database where name
matches the argument
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    sql_command = "SELECT * \
                    FROM states \
                    WHERE name LIKE '{:s}' ORDER BY id ASC".format(argv[4])
    cursor.execute(sql_command)
    result = cursor.fetchall()
    for state in result:
        if state[1] == argv[4]:
            print(state)
    cursor.close()
    db.close()
