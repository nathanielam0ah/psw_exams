#!/usr/bin/env python

import time
import datetime

class FillingStation:
    current_volume = 200    #in litres
    current_sales = 0
    number_of_attendants = 5

class Attendance:
    name = None
    currentVolume = 0
    start_time = None

    def get_starting_time(self):
        start_time = datetime.datetime.now()

    def get_current_volume(self):
        currentVolume = FillingStation.current_volume

    attendance = {'Name': name, 'volume': currentVolume , 'start': start_time}

def get_change_in_volume():
    change_in_volume = FillingStation.current_volume - Attendance.currentVolume