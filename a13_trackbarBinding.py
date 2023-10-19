# import numpy as np
# import cv2 as cv

# img = np.zeros((300, 512, 3), np.uint8)
# cv.namedWindow("Window")


# def go(x):
#     return x


# cv.createTrackbar("B", "Window", 10, 255, go)
# cv.createTrackbar("G", "Window", 10, 255, go)
# cv.createTrackbar("R", "Window", 10, 255, go)

# switch = "0 : OFF\n 1 : ON"

# cv.createTrackbar(switch, "Window", 0, 1, go)

# while 1:
#     cv.imshow("Window", img)
#     k = cv.waitKey(1) & 0xFF
#     if k == 27:
#         break

#     b = cv.getTrackbarPos("B", "Window")
#     g = cv.getTrackbarPos("G", "Window")
#     r = cv.getTrackbarPos("R", "Window")
#     s = cv.getTrackbarPos(switch, "Window")

#     if s == 0:
#         img[:] = 0
#     else:
#         img[:] = [b, g, r]


# cv.destroyAllWindows()













import numpy as np
import cv2 as cv

# img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow("Window")


def go(x):
    return x


cv.createTrackbar("CP", "Window", 10, 400, go)

switch = "color/gray"

cv.createTrackbar(switch, "Window", 0, 1, go)

while 1:
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    
    img=cv.imread('data/lena.jpg')
    pos = cv.getTrackbarPos("CP", "Window")
    font=cv.FONT_HERSHEY_TRIPLEX
    cv.putText(img, str(pos), (50, 150), font, 6, (0, 0, 255), 10)
    s = cv.getTrackbarPos(switch, "Window")

    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow("Window", img)

cv.destroyAllWindows()
