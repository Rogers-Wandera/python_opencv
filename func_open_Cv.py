import cv2 as cv

img = cv.imread("images/Aaron_Eckhart.jpg")
cv.imshow("original", img)

# gray scale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# blur
blur = cv.GaussianBlur(img, (7, 1), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# edges
edges = cv.Canny(img, 100, 122)
cv.imshow('edges', edges)

# dilation
dilate = cv.dilate(edges, (7, 7), iterations=1)
cv.imshow('dilate', dilate)

# eroding
erode = cv.erode(dilate, (7, 7), iterations=1)
cv.imshow('erode', erode)

# resizing
resized = cv.resize(img, (300, 300), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

# croping
croped = img[70:200, 100:300]
cv.imshow('cropped', croped)
cv.waitKey(0)
