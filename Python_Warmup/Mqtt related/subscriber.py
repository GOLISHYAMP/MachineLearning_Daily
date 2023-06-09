# Subscriber
import cv2
import numpy as np
import paho.mqtt.client as mqtt
import time
from PIL import Image
import base64

# MQTT broker configuration
broker_address = "10.236.76.215"  # Replace with your broker address
broker_port = 1883  # Default MQTT port
topic = "camera/live_streaming"




# Read the image file
# image_path = 'C:\\Users\\SPURUSHO\\Desktop\\Machine Learning\\MachineLearning_Daily\\Python_Warmup\\Mqtt related\\black-screen-blank.jpg'  # Replace with the path to your image
# image1 = cv2.imread(image_path)
image1 = None
# Callback function to process received messages
def on_message(client, userdata, message):
    byte_array = base64.b64decode(message.payload)
    
    np_array = np.frombuffer(byte_array, dtype=np.uint8)

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
    # print("Before")
    if image1 is not None:
        cv2.imshow("Image", image1)
    # print("I am in while loop")
        cv2.waitKey(1)
 
    # time.sleep(0.8)
    
    # pass  # Add any additional processing or logic here

# Stop the MQTT client loop
cv2.destroyAllWindows()
client.loop_stop()
