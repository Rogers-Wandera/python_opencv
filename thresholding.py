import cv2 as cv
import numpy as np

img = cv.imread("images/aroneckhart_2.jpg")

newimage = cv.resize(img, (500, 500))
cv.imshow("resized", newimage)

gray = cv.cvtColor(newimage, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('thresh image', thresh)

threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow('thresh image inv', thresh_inv)

# adaptive threshholding
adaptive = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive', adaptive)

cv.waitKey(0)
