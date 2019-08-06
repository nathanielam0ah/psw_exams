#!/usr/bin/env python
from datetime import date, datetime

class Customer:
    li = {}

    def get_CustomerInfo(self):             #recieves input of customer details.
        customerName = str(input("NAME: "))
        phone_number = str(input("PHONE NO: "))
        email = str(input("EMAIL: "))
        twitterUsername = str(input("TWITTER USERNAME: "))
        carNo = str(input("CAR NO: "))
        today = date.today()
        now = datetime.now()
        serviceDate = today.strftime("%d/%m/%Y")
        serviceTime = now.strftime("%H:%M:%S")
        li2 = {'DATE':serviceDate, 'TIME':serviceTime, 'NAME':customerName, 'PHONE NUMBER':phone_number, 'EMAIL':email, 'TWITTER USERNAME':twitterUsername, 'CAR NUMBER':carNo}
        Customer.li = li2

    def save_CustomerInfo(self):                #writes customer information to file
        writer = open("HistoryLog.md", "a+")
        writer.write(str(Customer.li))
        writer.write("\n")
        writer.close()
