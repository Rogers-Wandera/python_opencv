import numpy as np
import cv2 as cv

img = cv.imread("images/aroneckhart_2.jpg")
newimage = cv.resize(img, (500, 500))
cv.imshow("image", newimage)

blank = np.zeros(newimage.shape[:2], dtype='uint8')

# channels b,g,r
b, g, r = cv.split(newimage)

red = cv.merge([blank, blank, r])
green = cv.merge([blank, g, blank])
blue = cv.merge([b, blank, blank])

cv.imshow("red", red)
cv.imshow("green", green)
cv.imshow("blue", blue)

print(img.shape)
print(newimage.shape)
print(r.shape)
print(g.shape)
print(b.shape)

merged = cv.merge([b, g, r])
merged_2 = cv.merge([blue, green, red])
cv.imshow('merged_2', merged)
cv.imshow("merged", merged)
print(merged.shape)

cv.waitKey(0)
