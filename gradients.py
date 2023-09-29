import cv2 as cv
import numpy as np

img = cv.imread("images/aroneckhart_2.jpg")

newimage = cv.resize(img, (500, 500))
cv.imshow("resized", newimage)

gray = cv.cvtColor(newimage, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)

# sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined = cv.bitwise_or(sobelx, sobely)
canny = cv.Canny(gray, 10, 10)

cv.imshow("sobel x", sobelx)
cv.imshow("sobel y", sobely)
cv.imshow("combined", combined)
cv.imshow("canny", canny)
cv.waitKey(0)
