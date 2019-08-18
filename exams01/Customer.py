#!/usr/bin/env python3

from datetime import date, datetime
from mysql_module00 import mydb,mycursor
from mysql_module01 import mydb01, mycursor01

class Customer:
    li = ()

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
        li2 = (Name, phone_number, email, twitterUsername, carNo, serviceDate, serviceTime)
        Customer.li = li2
        return Customer.li

    def create_customer_database(self):              #creates a database for customers
        try:
            mycursor.execute("CREATE DATABASE deletemelater")
        except:
            None

    def save_customer_info(self):                #writes customer information to database
        try:
            mycursor01.execute("CREATE TABLE customer (name VARCHAR(255), phone VARCHAR(15), email VARCHAR(255), twitter VARCHAR(255), carNo VARCHAR(10), date VARCHAR(255), time VARCHAR(255))")
        except:
            None
        sqlFormula = "INSERT INTO customer (name, phone, email, twitter, carNo, date, time) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        customer = Customer.li
        mycursor01.execute(sqlFormula, customer)
        mydb01.commit()

if __name__ == "__main__":
    testCustomer = Customer()
    testCustomer.get_customer_info()
    testCustomer.create_customer_database()
    testCustomer.save_customer_info()
