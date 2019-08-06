#!/usr/bin/env python

from datetime import date, datetime
import getpass

#importing local modules
from Customer import Customer
from Management import ManagementLog
from CarWash import Wash
import SendEmail
import config

class Main:
    password = None

    def get_menu(self):
        print("CAR WASH APPLICATION")
        print("ENTER 1 FOR CUSOMER INFORMATION, 2 FOR START CAR WASH, 3 FOR ADMINISTRATOR LOG 4 TO EXIT MENU TERMINAL")
        try:
            menuInput = int(input(": "))
        except ValueError:
            print("INVALID INPUT")
        if menuInput == 1 :
            testApp = Customer()
            testApp.get_CustomerInfo()
            testApp.save_CustomerInfo()
        elif menuInput == 2:
            testApp = Wash(False)
            testApp.wash_car()
            testApp.notify()
        elif menuInput == 3:
            print("ENTER MANAGEMENT PASSWORD")
            password = getpass.getpass("PASSWORD: ")
            if password == config.management_pass:
                try:
                    testApp = ManagementLog()
                    testApp.readfile()
                except:
                    print("COULD NOT READ LOG FILE. NO LOG OR INCORRECT PASSWORD")
        elif menuInput == 4:
            exit()

if __name__ == "__main__":
    MainObject = Main()
    while 1:
        MainObject.get_menu()
