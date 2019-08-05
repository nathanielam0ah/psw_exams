#!/usr/bin/env python

from datetime import date, datetime
import threading

#importing local modules
from Customer import Customer
from Car import Wash
import SendEmail

class Main:
    def get_menu(self):
        print("CAR WASH APPLICATION")
        print("ENTER 1 FOR CUSOMER INFORMATION, 2 FOR START CAR WASH")
        try:
            menuInput = int(input(": "))
        except ValueError:
            print("INVALID INPUT")

        if menuInput == 1:
            testApp = Customer()
            testApp.get_CustomerInfo()
            testApp.save_CustomerInfo()
        elif menuInput == 2:
            testApp = Wash(False)
            testApp.wash_car()
            testApp.notify()
