#!/usr/bin/python3
"""
List all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Include {} <username> <pasword> <db name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db_query = 'SELECT * FROM states ORDER BY id ASC;'

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    cursor.execute(db_query)

    fetch = cursor.fetchall()

    for row in fetch:
        print(row)

        cursor.close()
        db.close()
