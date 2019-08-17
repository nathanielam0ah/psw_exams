#!/usr/bin/env python3

import mysql.connector
from config import host,user,password,database

mydb01 = mysql.connector.connect(
  host=host,
  user=user,
  passwd=password,
  database=database
)

mycursor01 = mydb01.cursor()
