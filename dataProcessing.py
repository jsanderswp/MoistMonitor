import csv
import time
import serial

# twilio implementation
from twilio.rest import Client

account_sid = 'AC09190c2e1005f08c38b13b61d2f3fab2'
auth_token = 'c230b92bcb6a4b9f2b320addb9b4e260'
client = Client(account_sid, auth_token)

threshold = 400  # Example moisture threshold

def check_moisture_and_notify():
    with open("moistureData.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                value = int(row[0])  # Adjust index if more columns exist
                if value < threshold:
                    message = client.messages.create(messaging_service_sid='MG5f417675f7ec606293dce1bd89ac59eb',
                    body='This is being sent thru Python!',
                    to='+18777804236'
                    )
                    print(f"Message sent: {message.sid}")
                    break
            except ValueError:
                pass
                
        

# function: read_serial data

def read_serial_data():
    ser = serial.Serial('/dev/cu.usbmodem1101', 115200, timeout=1)
    with open("moistureData.csv", "a+") as f:
        writer = csv.writer(f, delimiter=',')

        for i in range(100):
            s = ser.readline().decode()
            if s != "":
                rows = [int(x) for x in s.split(',')]
                writer.writerow(rows)
                f.flush()

def main():
    read_serial_data()
    check_moisture_and_notify()
main()
