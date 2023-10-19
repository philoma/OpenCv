import cv2
cap=cv2.VideoCapture(0)

# cv2.CAP_PROP_FRAME_WIDTH =3 in representation

cap.set(3, 1208)
cap.set(4, 720)

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    ret, frame=cap.read()
    if ret==True:
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break