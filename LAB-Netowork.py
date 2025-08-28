import serial
import time
import requests

SERIAL_PORT = '/dev/ttyAMA0'
BAUD_RATE = 115200
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)

while True:

    line = ser.readline().decode('utf-8').rstrip()
    url = f'https://iot-backend-iihizzkyh-nat-siriruangbuns-projects.vercel.app/data/Distance?amount={line}'
    requests.post(url)
    time.sleep(10)
