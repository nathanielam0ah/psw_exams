#!/usr/bin/env python3

def Logging (filename, error):
    f = open(filename, 'a+')
    f.write(str(error))
    f.close()

def readingLog (filename):
    r = open(filename, 'r')
    errors = r.read()
    for x in errors:
        print(x)