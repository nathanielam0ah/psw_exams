#!/usr/bin/env python
import time
import config
from SendEmail import send_email

class Wash:
    def __init__(self, washingDone):
        self.washingDone = washingDone

    def wash_car(self):
        try:
            print("Starting ...\nWashing Car ...")
            time.sleep(5)
            print("Done.")
            self.washingDone = True
            return self.washingDone
        except:
            self.washingDone = False
            return washingDone

    def notify(self):
        if self.washingDone == True:
            message = "Hello {name}, don/'t forget to pick up your car".format(name = "Customer")
            send_email("CAR WASH", message, config.email_client)
        else:
            print("FACING ISSUES CHECK IN LATER")
