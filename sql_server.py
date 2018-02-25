#!/usr/bin/env python

import pyodbc
server = '192.168.1.88'
database = 'SmartOffice'
username = 'hackathon2'
password = 'joshlabs'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

print('Reading data from table')

tsql = "SELECT UserId, LogDate, Direction FROM DeviceLogs_2_2018 " \
       "where logdate > Convert(datetime, '2018-02-25 17:01:25');"

# tsql = "SELECT UserId, LogDate, Direction FROM DeviceLogs_2_2018;"
with cursor.execute(tsql):
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
        row = cursor.fetchone()