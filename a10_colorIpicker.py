import numpy as np
import cv2

def click_event(event, x, y, flags, params):
    if event==cv2.EVENT_LBUTTONDOWN: # if press left button
        
        blue=img[y, x, 0]
        green=img[y, x, 1]
        red=img[y, x, 2]
        cv2.circle(img, (x,y), 3, (0, 0, 255), -1)
        mycolorimg=np.zeros((512, 512, 3), np.uint8)
        mycolorimg[:]=[blue, green, red]        

        cv2.imshow('Picked_color-', mycolorimg)


    
# img=np.zeros((512, 512, 3), np.uint8)
img=cv2.imread('data/lena.jpg')
cv2.imshow('Window', img)
points=[]
cv2.setMouseCallback('Window', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()