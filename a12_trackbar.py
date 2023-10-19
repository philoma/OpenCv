import cv2
import numpy as np
def getscore(x):
    print(x)
     
img=np.zeros((300, 300, 3), np.uint8)

cv2.namedWindow('Trackbar Window')

cv2.createTrackbar('B', 'Trackbar Window', 0, 255, getscore) 
cv2.createTrackbar('G', 'Trackbar Window', 0, 255, getscore)
cv2.createTrackbar('R', 'Trackbar Window', 0, 255, getscore)


while(1):
    cv2.imshow('Trackbar Window', img)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break
    else:
        b=cv2.getTrackbarPos('B', 'Trackbar Window')
        g=cv2.getTrackbarPos('G', 'Trackbar Window')
        r=cv2.getTrackbarPos('R', 'Trackbar Window')
        img[:]=[b, g, r]        

        

cv2.destroyAllWindows()