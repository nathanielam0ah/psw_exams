#!/usr/bin/env python

class ManagementLog:

    def readfile(self):
        readLog = eval(open('HistoryLog.md', 'r').read())
        print(readLog)

RetrieveLog = ManagementLog()
RetrieveLog.readfile()
