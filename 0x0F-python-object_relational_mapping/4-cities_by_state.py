#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    city_db = MySQLdb.connect(user = sys.argv[1], passwd = sys.argv[2]
            host = 'localhost', port = 3306, db = sys.argv[3])

    cursor = city_db.cursor()
    cursor.execute('SELECT cities.name, cities.id, states.name \
            FROM cities JOIN states ON cities.states_id ORDER BY \
            cities.id ASC')

    cities = cursor.fetchall()

    for city in cities:
        print(city)
