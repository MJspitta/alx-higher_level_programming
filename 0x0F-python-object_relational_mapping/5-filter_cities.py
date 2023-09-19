#!/usr/bin/python3
"""takes in the name of a state as argument and lists all cities of that state
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    query_cmd = """SELECT cities.name \
                    FROM states \
                    INNER JOIN cities ON states.id = cities.state_id \
                    WHERE states.name LIKE %s \
                    ORDER BY cities.id ASC"""
    cursor.execute(query_cmd, (argv[4],))
    result = cursor.fetchall()
    print(', '.join(["{:s}".format(city[0]) for city in result]))
    cursor.close()
    db.close()
