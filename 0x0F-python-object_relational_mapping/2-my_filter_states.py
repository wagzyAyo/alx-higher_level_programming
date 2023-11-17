#!/usr/bin/python3
"""
takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    my_db = sys.argv[3]
    name_searched = sys.argv[4]
    query = 'SELECT * FROM states WHERE LIKE BINARY {} ORDER BY id ASC'.format(
        name_searched)

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=my_db)

    cursor = db.cursor()
    cursor.execute(query)
    searched = cursor.fetchall()

    for item in searched:
        print(item)
