import numpy as np
import cv2 as cv

img = cv.imread("images/aroneckhart_2.jpg")
newimage = cv.resize(img, (500, 500))
cv.imshow("image", newimage)

blank = np.zeros(newimage.shape[:2], dtype='uint8')
cv.imshow("blank", blank)

circle = cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 200, 255, -1)
cv.imshow("circle", circle)

masked = cv.bitwise_and(newimage, newimage, mask=circle)
cv.imshow("masked", masked)
cv.waitKey(0)
