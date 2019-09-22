#!/usr/bin/env python3

import mysql.connector
from config import host,user,password

mydb = mysql.connector.connect(
  host=host,
  user=user,
  passwd=password,
)

mycursor = mydb.cursor()

class manageDB:
    def createDB (self, name):
        mycursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(name))

    def createTB (self, database, table,):
        mycursor.execute("USE {}".format(database))
        mycursor.execute("CREATE TABLE IF NOT EXISTS {} (name VARCHAR(255), phone VARCHAR(15), email VARCHAR(255), twitter VARCHAR(255), carNo VARCHAR(10), date VARCHAR(255), time VARCHAR(255))".format(table))

    def insertTB (self, database, table, list):
        mycursor.execute("USE {}".format(database))
        sqlFormula = "INSERT INTO Customers (name, phone, email, twitter, carNo, date, time) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(sqlFormula, list)
        mydb.commit()

    def readTB(self, database, table, item):
        mycursor.execute("USE {}".format(database))
        mycursor.execute("SELECT {} FROM {}".format(item, table))
        myresult = mycursor.fetchall()
        for row in myresult:
            print(row)