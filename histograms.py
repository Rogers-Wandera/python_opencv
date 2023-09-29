import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("images/aroneckhart_2.jpg")

newimage = cv.resize(img, (500, 500))
cv.imshow("resized", newimage)

blank = np.zeros(newimage.shape[:2], dtype='uint8')
# cv.imshow('blank', blank)

# gray_Scale = cv.cvtColor(newimage, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray_Scale)

mask = cv.circle(
    blank, (newimage.shape[1]//2, newimage.shape[0]//2), 100, 255, -1)
cv.imshow('mask', mask)

masked = cv.bitwise_and(newimage, newimage, mask=mask)
cv.imshow('masked', masked)

# gray_hist = cv.calcHist([gray_Scale], [0], mask, [256], [0, 256])

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

colors = ("b", "g", "r")

for i, col in enumerate(colors):
    print(f"i: {i}, col: {col}")
    img_hist = cv.calcHist([newimage], [i], mask, [255], [0, 255])
    plt.plot(img_hist, color=col)
    plt.xlim([0, 256])
plt.show()


cv.waitKey(0)
