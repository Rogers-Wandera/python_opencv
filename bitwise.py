import numpy as np
import cv2 as cv

blank = np.zeros((500, 500), dtype='uint8')
cv.imshow('blank', blank)

rectangle = cv.rectangle(blank.copy(), (50, 50), (450, 450), 255, -1)
circle = cv.circle(blank.copy(), (250, 250), 250, 255, -1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

# return intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('bitwise_and', bitwise_and)

# return non intersecting regions and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise_or", bitwise_or)

# returns non intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise_xor', bitwise_xor)

# returns not occupied regions
bitwise_not = cv.bitwise_not(circle)
cv.imshow('bitwise_not', bitwise_not)
cv.waitKey(0)
