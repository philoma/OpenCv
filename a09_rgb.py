import numpy as np
import cv2

def click_event(event, x, y, flags, params):
    if event==cv2.EVENT_LBUTTONDOWN: # if press left button
        print(x, ', ', y)
        font=cv2.FONT_HERSHEY_COMPLEX
        strXY=str(x)+", "+str(y)
        frame=cv2.putText(img, strXY, (x, y), font, .3, (255, 255, 0), 1)
        cv2.imshow('Coordinates', frame)
    if event==cv2.EVENT_FLAG_RBUTTON: # returns the bgr value of that pixle, works like a color picker
        blue=img[y, x, 0]
        green=img[y, x, 1]
        red=img[y, x, 2]

        font=cv2.FONT_HERSHEY_SIMPLEX
        strBGR=str(blue)+', '+str(green)+', '+str(red)

        cv2.putText(img, strBGR, (x, y), font, 0.5, (0, 255, 255), 1)

        cv2.imshow('Coordinates', img)


    
# img=np.zeros((512, 512, 3), np.uint8)
img=cv2.imread('data/messi5.jpg')

cv2.imshow('Coordinates', img)

cv2.setMouseCallback('Coordinates', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
