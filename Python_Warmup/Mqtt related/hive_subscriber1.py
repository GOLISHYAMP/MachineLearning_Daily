import paho.mqtt.client as mqtt

# MQTT broker information
broker_address = "172.29.98.241"
broker_port = 1883

# Create an MQTT client
client = mqtt.Client()

# Callback function for when a connection is established
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe("mytopic")

# Callback function for when a message is received
def on_message(client, userdata, msg):
    print("Received message: " + msg.payload.decode())

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Loop to process incoming messages
client.loop_forever()
