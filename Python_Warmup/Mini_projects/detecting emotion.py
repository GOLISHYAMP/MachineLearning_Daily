import cv2
from fer import FER



img = cv2.imread("C:\\Users\\SPURUSHO\\Desktop\\Machine Learning\\MachineLearning_Daily\\Python_Warmup\\Mini_projects\\SmileFace.jpg")
emotion = FER.detect_emotions(img)
print(emotion)
cv2.imshow("smile",img)
cv2.waitKey(0)
cv2.destroyAllWindows()