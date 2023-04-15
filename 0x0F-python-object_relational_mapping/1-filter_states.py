#!/usr/bin/python3
"""
A script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

iif __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states
                   WHERE name LIKE 'N%'
                   ORDERED BY id ASC")
    tables = cursor.fetchall()
    for table in tables:
        print(table)
    db.close()
