#!/usr/bin/env python3

from datetime import date, datetime
from Database import mydb, mycursor, manageDB

class Customer:
    list = []

    def get_customer_info(self):             #recieves input of customer details.
        Name = str(input("NAME: "))
        phone_number = str(input("PHONE NO: "))
        email = str(input("EMAIL: "))
        twitterUsername = str(input("TWITTER USERNAME: "))
        carNo = str(input("CAR NO: "))
        today = date.today()
        now = datetime.now()
        serviceDate = today.strftime("%d/%m/%Y")
        serviceTime = now.strftime("%H:%M")
        Customer.list = [Name, phone_number, email, twitterUsername, carNo, serviceDate, serviceTime]
        return Customer.list

    def save_customer_info(self):                #writes customer information to database
        database_object = manageDB()
        database_object.createDB('Car_Wash')
        database_object.createTB('Car_Wash', 'Customers')
        database_object.insertTB('Car_Wash', 'Customers', Customer.list)

if __name__ == "__main__":
    testCustomer = Customer()
    testCustomer.get_customer_info()
    testCustomer.save_customer_info()
