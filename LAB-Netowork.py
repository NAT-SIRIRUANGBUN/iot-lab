import serial
import time

SERIAL_PORT = '/dev/serial0' # ตรวจสอบให้แน่ใจว่าถูกต้อง
BAUD_RATE = 115200
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)

while True:

    line = ser.readline().decode('utf-8').rstrip()
    print(f"Received from ESP32: {line}")
