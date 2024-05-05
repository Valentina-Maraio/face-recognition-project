import cv2
import os
#from deepface import DeepFace

detected = 'assets/last_seconds_scene'
if not os.path.exists(detected):
    os.makedirs(detected)

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

video_path = "assets/last_seconds.mp4"
video_capture = cv2.VideoCapture(video_path)


def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(50, 50))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces


i = 0

while True:

    result, video_frame = video_capture.read()
    if result is False:
        break

    faces = detect_bounding_box(
        video_frame
    )

    cv2.imshow("My Face Detection Project", video_frame)

    filename = os.path.join(detected, 'detected_face{:>05}.jpg'.format(i))
    cv2.imwrite(filename, video_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    i += 1


video_capture.release()
cv2.destroyAllWindows()