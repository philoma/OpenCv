import cv2 as cv

img1 = cv.imread('data/lena.jpg')
cv.imshow('Window1', img1)

img2 = cv.imread('data/lena.jpg', 0)
cv.imshow('Window2', img2)

img3 = cv.imread('data/lena.jpg', -1)
cv.imshow('Window3', img3)

k = cv.waitKey(0) &0xFF  # The parameter of this function is the number of miliseconds the function waits for a keypress
# k- ascii rep of that key being pressed
if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('data/lenaCopy.png', img1)
