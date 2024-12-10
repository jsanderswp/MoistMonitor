import csv
import time
import serial

# twilio implementation
from twilio.rest import Client

account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

threshold = 300  # Example moisture threshold

def check_moisture_and_notify():
    with open("moistureData.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                value = int(row[0])  # Adjust index if more columns exist
                if value < threshold:
                    message = client.messages.create(
                        body="Your plant needs watering!",
                        from_="+123456789",  # Twilio phone number
                        to="+987654321"  # User's phone number
                    )
                    print(f"Message sent: {message.sid}")
            except ValueError:
                pass

check_moisture_and_notify()

# function: read_serial data

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



