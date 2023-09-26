from sense_emu import SenseHat
import time
from datetime import datetime
import sqlite3

delay = 5

sense = SenseHat()
sense.clear()
conn = sqlite3.connect('SenseHATDBLab.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS data (
    Date_Time DATETIME,
    Humidity FLOAT,
    Temperature FLOAT,
    Pressure FLOAT
);
''')

while True:
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    humidity = sense.get_humidity()
    temp = sense.get_temperature()
    pressure = sense.get_pressure()
    c.execute("INSERT INTO data(Date_Time, Humidity, Temperature, Pressure) VALUES(?,?,?,?)", (date_time, humidity, temp, pressure))
    conn.commit()
    time.sleep(delay)
