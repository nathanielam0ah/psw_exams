#!/usr/bin/env python
from datetime import date

class Customer:
    li = {}

    def get_CustomerInfo(self):             #recieves input of customer details.
        try:
            customerName = str(input("NAME: "))
            phone_number = str(input("PHONE NO: "))
            email = str(input("EMAIL: "))
            twitterUsername = str(input("TWITTER USERNAME: "))
            carNo = str(input("CAR NO: "))
            serviceTime = date.today()
        except ValueError:
            print("INVALID INPUT")
        li2 = {'NAME':customerName, 'PHONE NUMBER':phone_number, 'EMAIL':email, 'TWITTER USERNAME':twitterUsername, 'CAR NUMBER':carNo, 'TIME':serviceTime}
        Customer.li = li2

    def save_CustomerInfo(self):                #writes customer information to file
        writer = open("HistoryLog.md", "w+")
        writer.write(str(Customer.li))
        writer.close()

newCustomer = Customer()
newCustomer.get_CustomerInfo()
newCustomer.save_CustomerInfo()
