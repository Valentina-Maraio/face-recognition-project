import cv2
import os

detected_folder = 'assets/detected'
if not os.path.exists(detected_folder):
    os.makedirs(detected_folder)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

ret, frame = cap.read()

if not ret:
    print("Error: Could not capture frame")
    exit()

cv2.imshow("Captured image", frame)
cv2.waitKey(0)

filename = os.path.join(detected_folder, "detected_face.jpg")
cv2.imwrite(filename, frame)

cap.release()
cv2.destroyAllWindows()

print("Image saved successfully to: ", filename)