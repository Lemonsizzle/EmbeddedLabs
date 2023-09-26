from sense_hat import SenseHat
import time
from datetime import datetime
from csv import writer

delay = 5

sense = SenseHat()
sense.clear()
with open('SenseHatData.csv', 'w', newline='') as f:
    data_writer = writer(f)
    data_writer.writerow(['Time','Humidity','Temperature','Pressure'])
    while True:
        date_time = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")        
        humidity = sense.get_humidity()
        temp = sense.get_temperature()
        pressure = sense.get_pressure()
        data_writer.writerow([date_time, humidity, temp, pressure])
        time.sleep(delay)
