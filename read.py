import numpy as np
import cv2 as cv

img = cv.imread("images/Aaron_Eckhart.jpg")
cv.imshow("aron", img)
cv.waitKey(0)

# capture = cv.VideoCapture(0)
video = cv.VideoCapture("videos/vid.mp4")

while True:
    # isTrue, frame = capture.read()
    isTrue, frame = video.read()
    # cv.imshow('video', frame)
    key = cv.waitKey(20)
    cv.imshow('video2', frame)
    # pressing key d will close the window
    if key & 0xFF == ord('d'):
        break
    # pressin esc closes the window
    if key == 27:
        break
# capture.release()
video.release()
cv.destroyAllWindows()
