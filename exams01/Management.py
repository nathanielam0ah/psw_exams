#!/usr/bin/env python

class ManagementLog:

    def readfile(self):
        readLog = open("HistoryLog.md", "r").read()
        print(readLog)

if __name__ == "__main__":
    testMan = ManagementLog()
    testMan.readfile()
