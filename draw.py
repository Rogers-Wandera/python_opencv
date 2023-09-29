import cv2 as cv
import numpy as np

img = cv.imread("images/Aaron_Eckhart.jpg")
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('img', blank)
# blank[:] = 0, 255, 0
# cv.imshow('green', blank)

# draw rectangle
rec = cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness=-1)

# circle
cv.circle(rec, (rec.shape[1]//2, rec.shape[0]//2),
          40, (0, 0, 255), thickness=-1)

# draw line
cv.line(rec, (0, 0), (250, 500), (255, 255, 255), thickness=3)
cv.imshow("rec", rec)

cv.putText(blank, "Hello Rogers", (0, 100),
           cv.FONT_ITALIC, 1.0, (0, 0, 0), 2)
cv.imshow("text", blank)
cv.waitKey(0)
