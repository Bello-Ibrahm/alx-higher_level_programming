#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa
where name matches the argument."""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         port=3306, passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""
        SELECT cities.id, cities.name
        FROM cities
        JOIN states
        ON cities.state_id = states.id
        WHERE states.name LIKE BINARY %(match)s""", {'match': argv[4]})
    rows = cur.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))

    cur.close()
    db.close()
