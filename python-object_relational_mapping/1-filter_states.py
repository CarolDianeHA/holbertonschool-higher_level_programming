#!/usr/bin/python3
"""Script that lists all states with a name starting with N from the db."""

import MySQLdb
import sys

if __name__ == "__main__":
    """Gather user input for MySQL credentials."""
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=db_name,
        port=3306)

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE\
             name LIKE 'N%' COLLATE utf8mb4_bin ORDER BY id ASC;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    db.close()
