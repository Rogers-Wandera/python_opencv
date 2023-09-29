import cv2 as cv
import numpy as np

img = cv.imread("images/group1.jpg")
cv.imshow("original", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

haar_cascade = cv.CascadeClassifier("har_face.xml")

face_rect = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=3)

print(f"Faces are {len(face_rect)} (s)")

for (x, y, w, h) in face_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
cv.imshow("detected faces", img)

cv.waitKey(0)
