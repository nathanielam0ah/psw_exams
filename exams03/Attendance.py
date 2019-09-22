#!/usr/bin/env python3

from datetime import date, datetime
from mysql_module00 import mydb, mycursor
from GasStation import Gas_Station

class Attendance:
    li = ()

    def get_attendant_information(self):
        name = str(input("NAME: "))
        currentVolume = float(input("CURRENT VOLUME: "))
        today = date.today()
        now = datetime.now()
        Date = today.strftime("%d/%m/%Y")
        Time = now.strftime("%H:%M")
        li2 = (name, currentVolume , Date, Time )
        Attendance.li = li2

    def create_attendance_database(self):
        try:
            mycursor.execute("CREATE DATABASE deletemelater")
        except:
            None

    def save_attendant_information(self):
        try:
            mycursor.execute("USE deletemelater")
            mycursor.execute("CREATE TABLE attendant (name VARCHAR(255), volume VARCHAR(20), date VARCHAR(20), time VARCHAR(20) ")
        except:
            None
        sqlFormula = "INSERT INTO attendant (name, volume, date, time) VALUES (%s, %s, %s, %s)"
        attendance = Attendance.li
        mycursor.execute(sqlFormula, attendance)
        mydb.commit()


if __name__ == "__main__":
    testAttendance = Attendance()
    testAttendance.get_attendant_information()
    testAttendance.create_attendance_database()
    testAttendance.save_attendant_information()
