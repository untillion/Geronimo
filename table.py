import sqlite3
import datetime
import random


conn = sqlite3.connect('countries.db')
c = conn.cursor()

def create_table():
    c.execute ('CREATE TABLE IF NOT EXISTS countryTable3(Country TEXT, Number of Members REAL, notes TEXT, alignment TEXT, Total Members REAL)')

def data_entry():
    c.execute("INSERT INTO countryTable3 VALUES('Country Name',8,'chair and secreatry included','Global North or South',8)")
    conn.commit()
    #c.close()
    #conn.close()

def dynamic_data_entry():
    keyboard = imputfromKeyboard()
    member = str(keyboard.country(keyboard))
    c.execute("INSERT INTO countryTable2 (countryName, member) VALUES (?,?)",
                  (string, real))
    conn.commit()
    c.close()
    conn.close()
    

def read_from_db():
    c.execute("SELECT * FROM countryTable3")
    data = c.fetchall()
    print(data)
    for row in c.fetchall():
       print(row)
       





create_table()
data_entry()
##for i in range(10):
##for countryName in Country.country:
        ##dynamic_data_entry()
        ##time.sleep(1)
read_from_db()


c.close()
conn.close()
