#!/usr/bin/env python

#date and time modules
import time #time.time()
import datetime #datetime.datetime.now()

#classes
class ManagementLog:
    serviceLog = {}
    def get_serviceLog(self, serviceLog_confirm):
        serviceLog_confirm = str(input("GET SERVICE LOG? (y)es/(n)o: "))
        if (serviceLog_confirm == "y"):
            print(serviceLog)
        elif (serviceLog_confirm == "n"):
            print("returning to main menu ...")

class InterfaceLog():

    def get_Customer(self):
        testInterfaceObject = Customer()
        testInterfaceObject.get_CustomerInfo5

    carWashing = None

class Customer:
    customerName = None
    carBrand = None
    carModel = None
    carColour = None
    carNo = None
    carType = None

    def get_CustomerInfo(self):
        Customer.customerName = str(input("NAME: "))
        getCarObject = Cars()
        getCarObject.get_CarDescription

class Cars(Customer):

    def get_CarDescription(self):
        def owner(self, owner):
            owner = Customer.customerName
        Cars.carBrand = str(input("BRAND: "))
        Cars.carModel = str(input("MODEL: "))
        Cars.carColour = str(input("COLOUR: "))
        Cars.carNo = str(input("CAR NO: "))
        Cars.carType = str(input("TYPE: "))

class Payment(Customer):
    def getPayment(self):
        paymentAmount = float(input("AMOUNT: "))

class Attendance:

    def __init__(self, date, servicetime):
        self.date = date
        self.serviceTime = serviceTime

class Service_personel:
    name = None

    def __init__(self, serviceID, isDone):
        self.serviceID = serviceID
        self.isDone = isDone

    def washingState(self):
        str(input("DONE?, (y)es/(n)o: "))
        while 1:
            if (washingState == "y"):
                print("DONE")
                break
            else:
                print("Waiting")

testObject = InterfaceLog()
testObject.get_Customer
