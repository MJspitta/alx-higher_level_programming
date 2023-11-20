#!/usr/bin/python3
""" script that lists all cities from the database """


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    sql_command = "SELECT cities.id, cities.name, states.name \
                    FROM states \
                    INNER JOIN cities ON states.id = cities.state_id \
                    ORDER BY cities.id ASC"
    cursor.execute(sql_command)
    result = cursor.fetchall()
    for city in result:
        print(city)
    cursor.close()
    db.close()
