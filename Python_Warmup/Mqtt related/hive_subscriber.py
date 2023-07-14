import paho.mqtt.client as mqtt

# MQTT broker information
broker_address = "tester-xe9do0.a01.euc1.aws.hivemq.cloud"
broker_port = 8883

# Create an MQTT client
client = mqtt.Client()
client.username_pw_set('labuser', 'D3clare!')
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
