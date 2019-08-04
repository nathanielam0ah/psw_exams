#!/usr/bin/env python

class Customer:
    customerName = None
    phone_number = None
    email = None
    twitterUsername = None
    carBrand = None
    carColour = None
    carNo = None
    li = []

    def get_CustomerInfo(self):         #recieves input of customer details.

        customerName = str(input("NAME: "))
        phone_number = str(input("PHONE NO: "))
        email = str(input("EMAIL: "))
        twitterUsername = str(input("TWITTER USERNAME: "))
        carNo = str(input("CAR NO: "))
        li2 = {'NAME':customerName, 'PHONE NUMBER':phone_number, 'EMAIL':email, 'TWITTER USERNAME':twitterUsername, 'CAR NUMBER':carNo}
        Customer.li.append(li2)
        print(Customer.li)

newCustomer = Customer()
newCustomer.get_CustomerInfo()
