import cv2

# Create a QRCodeDetector object
qr_detector = cv2.QRCodeDetector()

# Create a VideoCapture object to read from the camera
cap = cv2.VideoCapture(0)  # 0 represents the default camera, change it if you have multiple cameras

# Check if the camera was opened successfully
if not cap.isOpened():
    print("Unable to open the camera.")
    exit()
li = []
# Continuously read frames from the camera
while True:
    # Read the current frame from the camera
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if not ret:
        print("Unable to read the frame.")
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect and decode QR codes from the frame
    li.extend(qr_detector.detectAndDecodeMulti(gray_frame))

    
    if li[0]:
        if li[1][0]:
            print(li[1][0])
            break
    

    # Display the frame with QR code detections
    cv2.imshow("QR Code Detection", frame)
    li = []
    # Wait for the 'q' key to be pressed to exit
    if cv2.waitKey(1) == ord('q'):
        break

# Release the VideoCapture object and close the windows
cap.release()
cv2.destroyAllWindows()
