#!/usr/bin/python3
"""
A script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states\
                   WHERE name LIKE BINARY '{:s}'\
                   ORDER BY states.id ASC".format(argv[4]))
    tables = cursor.fetchall()
    for table in tables:
        if table[1] == argv[4]:
            print(table)
    cursor.close()
    db.close()
