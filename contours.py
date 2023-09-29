import numpy as np
import cv2 as cv

img = cv.imread("images/Aaron_Eckhart.jpg")
cv.imshow("original", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("blank", blank)

# blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)

canny = cv.Canny(img, 100, 100)
cv.imshow("canny", canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

contours, hierachies = cv.findContours(
    canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(blank, contours, -1, (255, 255, 0), 1)
cv.imshow("drawn contours", blank)

print(len(contours))
cv.waitKey(0)
