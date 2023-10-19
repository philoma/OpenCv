import cv2

img=cv2.imread('data/messi5.jpg')
img2=cv2.imread('data/lena.jpg')

print(img.shape)
print(img.size)
print(img.dtype)

b, g, r=cv2.split(img)

img=cv2.merge((b, g, r)) 

ball=img[280:340, 330:390]
img[273:333, 100:160]=ball

# ball=img[290:335, 337:312]
# img[273:333, 100:160]=ball
img=cv2.resize(img, (512, 512))
img2=cv2.resize(img2, (512, 512))
newimg=cv2.add(img, img2)
cv2.imshow('Window1', newimg)

newimg=cv2.addWeighted(img, 0.5, img2, 0.9, 0) # (img array, alpha, img2, beta, gamma) alpha, beta is weight of 1st,2nd img, beta is if any scaler value wanna add
cv2.imshow('Window2', newimg)

cv2.waitKey(0)
cv2.destroyAllWindows()