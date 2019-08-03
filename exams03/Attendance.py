#!/usr/bin/env python

import time
import datetime
from Gas_Station import GasStation

class Attendance:
    name = None
    currentVolume = 0
    start_time = None
    attendance = []

    def get_attendance(self):
        name = str(input("NAME: "))
        currentVolume = float(input("CURRENT VOLUME: "))
        start_time = datetime.datetime.now()
        attendance_1 = {'Name': name, 'volume': currentVolume , 'start': start_time}
        Attendance.attendance.append(attendance_1)
        print(attendance)
        
def get_change_in_volume():
    change_in_volume = GasStation.current_volume - Attendance.currentVolume

attendanceObject = Attendance()
attendanceObject.get_attendance()
