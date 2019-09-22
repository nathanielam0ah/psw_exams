#!/usr/bin/env python3

from Database import manageDB

class ManagementLog:

    def read_from_database(self):
        readTable = manageDB()
        item = str(input('Search Row Keyword: '))
        readTable.readTB('Car_Wash', 'Customers', item)

if __name__ == "__main__":
    testMan = ManagementLog()
    testMan.read_from_database()
