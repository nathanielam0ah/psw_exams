#!/usr/bin/env python

from mysql_module01 import mydb01, mycursor01

class ManagementLog:

    def read_from_database(self):
        mycursor01.execute("SELECT * FROM customer")
        myresult = mycursor01.fetchall()
        for row in myresult:
            print(row)

if __name__ == "__main__":
    testMan = ManagementLog()
    testMan.read_from_database()
