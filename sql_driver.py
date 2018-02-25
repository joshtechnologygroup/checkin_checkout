#!/usr/bin/env python

import pyodbc
server = '192.168.1.88'
database = 'SmartOffice'
username = 'hackathon2'
password = 'joshlabs'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


def execute(tsql):
    data = []
    with cursor.execute(tsql):
        data.append(cursor.fetchone())
    return data