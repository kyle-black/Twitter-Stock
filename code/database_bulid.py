import sqlite3
from sqlite3 import Error
import os
import config

con = sqlite3.connect(config.DB_FILE)

# print(config.DB_FILE)
#cursorObj = con.cursor()


def sql_connection():

    try:

        con = sqlite3.connect(config.DB_FILE)

        return con

    except Error:

        print(Error)


def sql_table(con):
    cursorObj = con.cursor()
    # cursorObj.execute(
    #    "CREATE TABLE IF NOT EXISTS stock(id INTEGER PRIMARY KEY,symbol TEXT NOT NULL UNIQUE,name TEXT NOT NULL,exchange TEXT NOT NULL)")

    cursorObj.execute(
        "CREATE TABLE IF NOT EXISTS cars(name TEXT NOT NULL UNIQUE PRIMARY KEY,tweets TEXT )")

    #cursorObj.execute('DROP TABLE cars')
    #cursorObj.execute("""CREATE TABLE IF NOT EXISTS stock""")
    #cursorObj.execute("""CREATE TABLE IF NOT EXISTS stock_price(id INTEGER PRIMARY KEY,symbol,stock_id INTEGER,date TEXT,open NOT NULL,high NOT NULL,low NOT NULL,close NOT NULL,volume NOT NULL,sma_20,sma_50,rsi_14, FOREIGN KEY (stock_id) REFERENCES stock (id))""")
    #cursorObj.execute('DROP TABLE stock_price')
   # / cursorObj.execute('DROP TABLE tranaction log')

    con.commit()


con = sql_connection()

sql_table(con)
