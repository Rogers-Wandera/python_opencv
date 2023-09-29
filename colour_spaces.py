import numpy as np
import cv2 as cv

img = cv.imread("images/aroneckhart_2.jpg")
newimage = cv.resize(img, (500, 500))
cv.imshow("image", newimage)

# BGR to GRAY
grayscale = cv.cvtColor(newimage, cv.COLOR_BGR2GRAY)
cv.imshow("gray", grayscale)

# BGR to HSV
hsv = cv.cvtColor(newimage, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# BGR to LAB
lab = cv.cvtColor(newimage, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# BGR to RGB
rgb = cv.cvtColor(newimage, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

# hsv to bgr
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("hsv_bgr", hsv_bgr)
cv.waitKey(0)
