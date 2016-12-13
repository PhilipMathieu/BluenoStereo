import sqlite3
import time

DATAPATH = './'


# setup bluetooth connection and get car vin
vin = "1234567890abcdefg"

# start up database
conn = sqlite3.connect(DATAPATH + 'cardata.db')
data = conn.cursor()
data.execute('''CREATE TABLE IF NOT EXISTS cars
    (car_id integer primary key, car_vin char(17) NOT NULL UNIQUE)''')
data.execute('''CREATE TABLE IF NOT EXISTS rpmdata
    (car_id integer, rpm integer, sample_time TIMESTAMP NOT NULL UNIQUE,
    FOREIGN KEY(car_id) REFERENCES cars(car_id))''')

# add car to database
data.execute('''INSERT OR IGNORE INTO cars (car_vin) VALUES (?) ''', (vin,))
# get car id
data.execute('''SELECT car_id FROM cars WHERE car_vin=?''', (vin,))
carid = data.fetchone()[0]

# fake some RPM data
rpm = 856
data.execute('''INSERT OR IGNORE INTO rpmdata (car_id, rpm, sample_time)
    VALUES (?,?,datetime('now')) ''', (carid, rpm))

conn.commit()
conn.close()
