#!/usr/bin/env python
import time
import config
from SendEmail import send_email
from Customer import Customer

class Wash:
    def __init__(self, washingDone):
        self.washingDone = washingDone

    def wash_car(self):
        try:
            print("Starting ...\nWashing Car ...")
            time.sleep(5)
            print("Done.")
            self.washingDone = True
        except:
            self.washingDone = False
        return self.washingDone
