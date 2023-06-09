import paho.mqtt.client as mqtt
import time
import cv2
import numpy as np
import base64


# MQTT broker configuration
broker_address = "10.236.76.215"  # Replace with your broker address
broker_port = 1883  # Default MQTT port
topic = "camera/live_streaming"

# Create an MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Publish temperature readings every 5 seconds



# Create a VideoCapture object to capture video from the default camera
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Failed to open the camera")
    exit()

while True:
    # temperature = 23.5  # Replace with your actual temperature reading
    # message = str(temperature) + "°C"
    ret, frame = cap.read()

    # If the frame is not read successfully, break the loop
    if not ret:
        print("Failed to read the frame")
        break

    # Display the frame in a window named "Live Stream"
    cv2.imshow("Live Stream", frame)
    _, image_bytes = cv2.imencode('.jpg', frame)
    byte_array = np.array(image_bytes).tobytes()

    base64_data = base64.b64encode(byte_array)
    # base64_string = base64_data.decode('utf-8') 
    # Print the byte array
    # print(byte_array)
    # message = str(type(frame))
    # Check for the 'q' key to quit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    client.publish(topic, base64_data)
    # print("Published: " + message)

    # time.sleep(5)  # Wait for 5 seconds before publishing the next reading


# Release the VideoCapture object and close the window
cap.release()
cv2.destroyAllWindows()
# Disconnect from the MQTT broker
client.disconnect()