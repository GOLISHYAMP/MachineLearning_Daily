import paho.mqtt.client as paho
from paho import mqtt

# MQTT broker information
broker_address = "tester-xe9do0.a01.euc1.aws.hivemq.cloud"
broker_port = 8883
def on_connect(client):
    print("Connected to MQTT broker")
    client.publish("topic", "message")
# Create an MQTT client
client = paho.Client(client_id="abc", userdata=None, protocol=paho.MQTTv5)
# client.username_pw_set('labuser', 'D3clare!')
client.on_connect = on_connect(client=client)
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

# Connect to the MQTT broker
client.connect(broker_address, broker_port)
    # print("Connected successfully")

    

# Topic to publish to
topic = "mytopic"

# Message to publish
message = "Hello, HiveMQ!"

# Publish the message
# while(True):
#     client.publish(topic, message)

# Disconnect from the MQTT broker
client.disconnect()
