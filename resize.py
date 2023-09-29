import cv2 as cv

capture = cv.VideoCapture(0)


def resizeFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


video = cv.VideoCapture("videos/vid.mp4")
image = cv.imread("images/aroneckhart_2.jpg")
resizedimg = resizeFrame(image, 0.40)
cv.imshow("img", image)
cv.imshow('img1', resizedimg)

while True:
    isTrue, frame = video.read()
    resized = resizeFrame(frame, .2)
    cv.imshow("vid", frame)
    cv.imshow("vid1", resized)
    isTrue, frame = capture.read()
    newframe = cv.resize(frame, (400, 500))
    cv.imshow("cam", newframe)

    key = cv.waitKey(20)
    if key & 0xFF == ord("d"):
        break
    if key == 27:
        break

video.release()
capture.release()
cv.destroyAllWindows()
