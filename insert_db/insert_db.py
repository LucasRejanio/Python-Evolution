#!/usr/bin/env python3

import cx_Oracle
import datetime
import time

MAX_DB_CONNECT_TRIES = 20
DATA_EXEC = time.strftime("%Y/%m/%d")

def conecta_banco(i=1):
    cursor, connection = None, None
    try:
        DB_USER = 'Username'
        DB_PASS = 'Password'
        DB_URL = 'end-point-rds'

        connection = cx_Oracle.connect(DB_USER, DB_PASS, DB_URL)
        cursor = connection.cursor()
    except cx_Oracle.DatabaseError as e:
        raise e
        i = i + 1
        print('Conectando com o Banco')
        if(i <= MAX_DB_CONNECT_TRIES):
            time.sleep(90)
            cursor, connection = conecta_banco(i)
        else:
            exit(-1)

    return cursor, connection

def insertDb():
    cursor, connection = conecta_banco()

    query = "INSERT INTO TABLE (COLUMNS) VALUES ()"

    try:
        cursor.execute(query)
        cursor.execute('commit')
        connection.commit()
        connection.close()
    except cx_Oracle.DatabaseError:
        exit(-1)

insertDb()
print('Query executada')



