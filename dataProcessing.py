import csv
import time
import serial

def read_serial_data():
    ser = serial.Serial('/dev/cu.usbmodem101', timeout=1)
    with open("moistureData.csv", "a+") as f:
        writer = csv.writer(f, delimiter=',')

        while True:
            s = ser.readline().decode()
            if s != "":
                rows = [int(x) for x in s.split(',')]
                print(rows)
                writer.writerow(rows)
                f.flush()
#left to do: iterate thru CSV, check for moisture values below threshold, send twilio message if so



