#!/usr/bin/env python3

import mysql.connector
from config import host,user,password

mydb = mysql.connector.connect(
  host=host,
  user=user,
  passwd=password,
)

mycursor = mydb.cursor()
