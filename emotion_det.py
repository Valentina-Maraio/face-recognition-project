import cv2
from fer import FER

emotion_detector = FER(mtcnn=True)
img = cv2.imread("assets/input_new.jpg")
img_resize = cv2.resize(img, (600, 600))

emotions = emotion_detector.detect_emotions(img_resize)
print(emotions)

top_emotion, emotion_score = emotion_detector.top_emotion(img_resize)
print(top_emotion, emotion_score)

cv2.imshow("Image's emotion", img_resize)

cv2.waitKey(0)
cv2.destroyAllWindows()
