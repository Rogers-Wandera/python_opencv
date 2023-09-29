import os
import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier("har_face.xml")

people = []
for i in os.listdir(r'D:\user\open_cv\images_2'):
    people.append(i)


#

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

img = cv.imread(
    r"D:\user\open_cv\images_2\Abdel_Aziz_Al-Hakim\Abdel_Aziz_Al-Hakim_0001.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in face_rect:
    face_roi = gray[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(face_roi)
    print(f"Label = {people[label]} with confidence of {confidence}")
    print(label)

    cv.putText(img, str(people[label]), (20, 20),
               cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=1)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=1)

cv.imshow("detected face", img)
cv.waitKey(0)
