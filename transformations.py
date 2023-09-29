import numpy as np
import cv2 as cv

img = cv.imread("images/aroneckhart_2.jpg")
img2 = cv.resize(img, (600, 600), cv.INTER_AREA)

cv.imshow('img', img2)


def translateImage(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


def rotateImage(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimesions = (width, height)
    return cv.warpAffine(img, rotMat, dimesions)


# -x -> left, -y -> up, +x -> right, +y -> down
trnaslated = translateImage(img2, -100, -50)
cv.imshow('translated', trnaslated)

# rotation
rotate = rotateImage(img2, 45)
cv.imshow('rotate', rotate)

# flipping
flip = cv.flip(img2, 0)
cv.imshow('flip', flip)

# cropping
crop = img[200:400, 300:400]
cv.imshow('cropped', crop)
cv.waitKey(0)
