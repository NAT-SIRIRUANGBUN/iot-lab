
import paho.mqtt.client as mqtt
import time

# The callback for when the client connects.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

# Create an MQTT client instance
client = mqtt.Client()

# Assign the callback functions
client.on_connect = on_connect

# Connect to the public broker
client.connect("test.mosquitto.org", 1883, 60)

# Start a non-blocking network loop
client.loop_start()

# Publish a message
try:
    while True:
        # Publish a message to the specified topic
        client.publish("rpi5/tutorial/test", "Hello from my Python script!")
        print("Message published.")
        time.sleep(5)  # Wait 5 seconds before publishing again
except KeyboardInterrupt:
    print("Exiting...")
    client.loop_stop()
    client.disconnect()

