import numpy as np
import cv2 as cv

def go(x):
    return x

cv.namedWindow('Track')

# cap=cv.VideoCapture(0)
cv.createTrackbar('LH','Track', 0, 255, go)
cv.createTrackbar('UH','Track', 0, 255, go)
cv.createTrackbar('LS','Track', 0, 255, go)
cv.createTrackbar('US','Track', 255, 255, go)
cv.createTrackbar('LV','Track', 255, 255, go)
cv.createTrackbar('UV','Track', 255, 255, go)

while True:

    k=cv.waitKey(1)
    if k==27:
        break

    frame=cv.imread('data/smarties.png')
    # _, frame=cap.read()

    hsv=cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lh=cv.getTrackbarPos('LH', 'Track')
    uh=cv.getTrackbarPos('UH', 'Track')
    ls=cv.getTrackbarPos('LS', 'Track')
    us=cv.getTrackbarPos('US', 'Track')
    lv=cv.getTrackbarPos('LV', 'Track')
    uv=cv.getTrackbarPos('UV', 'Track')

    l_b=np.array([lh, ls, lv])
    u_b=np.array([uh, us, uv])

    mask=cv.inRange(hsv, l_b, u_b) # thresholding the hsv img to get desired colrs only

    res=cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame', frame)
    cv.imshow('res', res )


# cap.release()
cv.destroyAllWindows()