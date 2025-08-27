import serial
import time

try:
    ser = serial.Serial(
        port='/dev/ttyS0', # Check your specific port
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    print("Serial port opened successfully.")
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    ser = None

if ser:
    try:
        # Give the connection time to establish
        time.sleep(2)
        
        while True:
            # Check if there is data in the serial buffer
            if ser.in_waiting > 0:
                # Read a line of data until a newline character is found
                line = ser.readline()
                
                # Decode the received bytes into a string
                data = line.decode('utf-8').strip()
                
                # Check if the data is a valid number
                try:
                    distance = float(data)
                    print(f"Received Distance: {distance} cm")
                except ValueError:
                    print(f"Received invalid data: {data}")
            
            # Pause for a moment to prevent a busy loop
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Exiting Program.")
    finally:
        if ser.is_open:
            ser.close()
            print("Serial port closed.")