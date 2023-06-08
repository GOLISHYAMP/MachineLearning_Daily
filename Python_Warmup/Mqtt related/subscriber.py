# Subscriber
import cv2
import numpy as np
import paho.mqtt.client as mqtt
import time
from PIL import Image

# MQTT broker configuration
broker_address = "10.236.76.215"  # Replace with your broker address
broker_port = 1883  # Default MQTT port
topic = "home/temperature"




# Read the image file
image_path = '..\\black-screen-blank.jpg'  # Replace with the path to your image
image1 = Image.open(image_path)
# Callback function to process received messages
def on_message(client, userdata, message):
    np_array = np.frombuffer(message.payload, dtype=np.uint8)

    # Decode the NumPy array into an image
    image = cv2.imdecode(np_array, flags=cv2.IMREAD_COLOR)

    # print("Received message: " + str(message.payload.decode()))
    global image1
    image1 = image

# Create an MQTT client
client = mqtt.Client()

# Set the callback function
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Subscribe to the topic
client.subscribe(topic)

# Start the MQTT client loop to receive messages
client.loop_start()

# Keep the subscriber script running
while True:
    cv2.imshow("Image", image1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # time.sleep(0.8)
    
    pass  # Add any additional processing or logic here

# Stop the MQTT client loop
client.loop_stop()
