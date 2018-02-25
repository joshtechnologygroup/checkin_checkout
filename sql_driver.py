#!/usr/bin/env python

import pyodbc

from retrying import retry

# database settings
server = '192.168.1.88'
database = 'SmartOffice'
username = 'hackathon2'
password = 'joshlabs'
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 13 for SQL Server};SERVER=' + server + ';PORT=1443;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()


@retry(stop_max_attempt_number=10, wait_random_min=1000, wait_random_max=2000)
def execute(sql):
    data = []
    with cursor.execute(sql):
        data.append(cursor.fetchone())
    return data
