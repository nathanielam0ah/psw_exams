#!/usr/bin/env python
import datetime

class Customer:
    li = []

    def get_CustomerInfo(self):             #recieves input of customer details.
        try:
            customerName = str(input("NAME: "))
            phone_number = str(input("PHONE NO: "))
            email = str(input("EMAIL: "))
            twitterUsername = str(input("TWITTER USERNAME: "))
            carNo = str(input("CAR NO: "))
            serviceTime = datetime.datetime.now()
        except ValueError:
            print("INVALID INPUT")
        li2 = {'NAME':customerName, 'PHONE NUMBER':phone_number, 'EMAIL':email, 'TWITTER USERNAME':twitterUsername, 'CAR NUMBER':carNo, 'TIME':serviceTime}
        Customer.li.append(li2)

newCustomer = Customer()
newCustomer.get_CustomerInfo()
