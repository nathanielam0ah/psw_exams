#!/usr/bin/env python3

import time
import config
from Customer import Customer
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
        except:
            self.washingDone = False
        return self.washingDone

if __name__ == "__main__":
    testWash = Wash(False)
    testWash.wash_car()
