import csv
import time
import serial

ser = serial.Serial('INSERT PORT NAME', timeout=1)

f = open("moistureData.csv", "a+")
writer = csv.writer(f, delimiter=', ')

while True:
    s = ser.readline().decode()
    if s != "":
        rows = [int(x) for x in s.split(', ')]
        print(rows)
        writer.writerow(rows)
        f.flush()

#left to do: iterate thru CSV, check for moisture values below threshold, send twilio message if so



