import cv2
cap=cv2.VideoCapture(0)
from datetime import datetime

while(cap.isOpened()):
    ret, frame=cap.read()
    if ret==True:
        text='Width: '+str(cap.get(3))+' Height: '+str(cap.get(4))
        font=cv2.FONT_HERSHEY_COMPLEX
        frame=cv2.putText(frame, text, (100, 100), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

        text=str(datetime.now())
        frame=cv2.putText(frame, text, (100, 200), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('Window', frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
