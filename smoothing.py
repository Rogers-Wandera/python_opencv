import numpy as np
import cv2 as cv

img = cv.imread("images/aroneckhart_2.jpg")
newimage = cv.resize(img, (500, 500))
cv.imshow("image", newimage)

# average blur
blur = cv.blur(newimage, (5, 5))
cv.imshow("average blur", blur)

# Gaussian blur
gauss = cv.GaussianBlur(newimage, (5, 5), 0)
cv.imshow("Gaussian blur", gauss)

# median blur
median = cv.medianBlur(newimage, 5)
cv.imshow("median blur", median)

# bileteral blur
bileteral = cv.bilateralFilter(newimage, 15, 10, 10)
cv.imshow("bileteral", bileteral)
cv.waitKey(0)
