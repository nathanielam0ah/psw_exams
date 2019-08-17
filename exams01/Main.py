#!/usr/bin/env python

from datetime import date, datetime
import getpass

#importing local modules
from Customer import Customer
from Management import ManagementLog
from SendEmail import send_email
from CarWash import Wash
from config import email_client, email_server, email_server_pass, management_pass
import SendSms

class Main:
    password = None

    def get_menu(self):
        print("CAR WASH APPLICATION")
        print("ENTER 1 FOR CUSTOMER INFORMATION, 2 FOR START CAR WASH, 3 FOR ADMINISTRATOR LOG 4 TO EXIT MENU TERMINAL")
        try:
            menuInput = int(input(": "))
        except ValueError:
            print("INVALID INPUT")
        if menuInput == 1 :
            testCustomer = Customer()
            testCustomer.get_customer_info()
            testCustomer.create_customer_database()
            testCustomer.save_customer_info()
        elif menuInput == 2:
            testWash = Wash(False)
            testWash.wash_car()
            if testWash.washingDone == True:
                message = "Hello {name}, don't forget to pick up your car".format(name = "Customer")
                send_email("CAR WASH", message, email_client)
            else:
                print("FACING ISSUES CHECK IN LATER")
        elif menuInput == 3:
            print("ENTER MANAGEMENT PASSWORD")
            password = getpass.getpass("PASSWORD: ")
            if password == management_pass:
                try:
                    testApp = ManagementLog()
                    testApp.read_from_database()
                except:
                    print("COULD NOT READ LOG FILE. NO LOG OR INCORRECT PASSWORD")
            else:
                print("INCORRECT PASSWORD")
        elif menuInput == 4:
            exit()

if __name__ == "__main__":
    MainObject = Main()
    while 1:
        MainObject.get_menu()
