import cv2

# cascade_path = cv2.data.haarcascades + 'haarcascade_eye.xml'
# cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
cascade_path = cv2.data.haarcascades + 'haarcascade_lefteye_2splits.xml'

cascade = cv2.CascadeClassifier(cascade_path)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Unable to open Camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Unable to read the image from camera")
        break
    print(type(frame),type(ret))
    gray_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    objects = cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in objects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow("Live Video", frame)

   
    if cv2.waitKey(1) == ord('q'):
        break

# Release the VideoCapture object and close the window
cap.release()
cv2.destroyAllWindows()
    