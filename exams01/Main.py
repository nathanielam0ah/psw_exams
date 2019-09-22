#!/usr/bin/env python3

import getpass
from datetime import date, datetime
from CarWash import Wash
from config import email_server, email_server_pass, management_pass
from Customer import Customer
from Logging import Logging
from Management import ManagementLog
from SendEmail import send_email
from SendSms import send_sms


class Main:
    password = None

    def get_menu(self):             #where the attendant interacts with the application
        print("CAR WASH APPLICATION")
        print("ENTER 1 TO ADD TO CUSTOMER LOG, 2 FOR START CAR WASH, 3 FOR ADMINISTRATOR LOG 4 TO EXIT MENU TERMINAL")
        try:
            menuInput = int(input(": "))
        except ValueError:
            print("INVALID INPUT")
        if menuInput == 1 :
            testCustomer = Customer()
            testCustomer.get_customer_info()
            testCustomer.save_customer_info()
            input()

        elif menuInput == 2:
            testWash = Wash(False)
            testWash.wash_car()
            if testWash.washingDone == True:
                try:
                    message = "Hello {}, don't forget to pick up your car".format(Customer.li[0])
                    send_email("CAR WASH", message, Customer.li[2])
                except:
                    print("ERRORxCUSOTOMER_NAMExEMAIL_EMPTY")
                try:
                    message = "Hello {}, don't forget to pick up your car".format(Customer.li[0])
                    send_sms(message,Customer.li[1])
                except:
                    print("ERRORxCUSOTMER_NAMExSMS_EMPTY. ")
                input()

        elif menuInput == 3:
            print("ENTER MANAGEMENT PASSWORD")
            password = getpass.getpass("PASSWORD: ")
            if password == management_pass:
                try:
                    testApp = ManagementLog()
                    testApp.read_from_database()
                    input()
                except:
                    print("COULD NOT READ DATABASE. NO RESULT")
            else:
                print("INCORRECT PASSWORD")

        elif menuInput == 4:
            exit()

if __name__ == "__main__": # where the Main class is instantiated
    MainObject = Main()
    while 1:
        try:
            MainObject.get_menu()
        except Exception as error:
            Logging(error.log, error)
