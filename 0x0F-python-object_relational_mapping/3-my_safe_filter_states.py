#!/usr/bin/python3
""" script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
But one that is safe from MySQL injections
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
    sql_command = """SELECT * \
                     FROM states \
                     WHERE name=%s ORDER BY id ASC"""
    cursor.execute(sql_command, (argv[4],))
    result = cursor.fetchall()
    for state in result:
        print(state)
    cursor.close()
    db.close()
