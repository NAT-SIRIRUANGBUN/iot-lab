import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect, our subscriptions will be renewed.
    client.subscribe("rpi5/tutorial/test")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(f"Topic: {msg.topic}, Message: {msg.payload.decode()}")

# Create an MQTT client instance
client = mqtt.Client()

# Assign the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the public broker
client.connect("test.mosquitto.org", 1883, 60)

# This loop processes network traffic, calls callbacks, and handles reconnecting.
client.loop_forever()