import paho.mqtt.client as mqtt

# MQTT broker information
broker_address = "172.29.98.241"
broker_port = 1883

# Create an MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Topic to publish to
topic = "mytopic"

# Message to publish
message = "Hello, HiveMQ!"

# Publish the message
while(True):
    client.publish(topic, message)

# Disconnect from the MQTT broker
client.disconnect()
