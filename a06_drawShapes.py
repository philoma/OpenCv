import numpy as np
import cv2
# img=cv2.imread('data/lena.jpg',1)
img=np.zeros([512, 512, 3], np.uint8)

img=cv2.line(img, (0, 0), (255, 255), (0, 5, 12), 2) # (img, (x1, y1), (x2, y2), (b g r), thickness(in px))
img=cv2.arrowedLine(img, (1, 9), (34, 255), (76, 5, 12), 5) # (img, (x1, y1), (x2, y2), (b g r), thickness)
img=cv2.rectangle(img, (200, 200), (300, 300), (0, 255, 0), 8)
img=cv2.rectangle(img, (210, 210), (290, 290), (0, 255, 0), -1)
img=cv2.circle(img, (340, 340), 52, (0, 0, 255), -1)
font=cv2.FONT_HERSHEY_COMPLEX
img1=cv2.putText(img, 'Hello World', (100, 200), font, 2, (255, 255, 255), 10, cv2.LINE_AA)
cv2.imshow('The Image Window', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
