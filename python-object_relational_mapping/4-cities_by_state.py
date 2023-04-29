#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa."""

import MySQLdb
import sys

if __name__ == "__main__":
    """Gather user input for MySQL credentials."""
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    # state = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=db_name,
        port=3306)

    cursor = db.cursor()
    querty = "SELECT cities.id, cities.name, states.name FROM cities \
              JOIN states ON cities.state_id = states.id \
              ORDER BY cities.id ASC"
    cursor.execute(querty,)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    db.close()
