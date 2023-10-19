# OpenCV Python Tutorial For Beginners 4 - How to Read, Write, Show Videos from Camera in OpenCV
# import cv2

# cap = cv2.VideoCapture(0)  # index of camera(-1/0, 1, 2, 3,...) # or any video file path to wrk on

# while True:
#     ret, frame = cap.read()

#     cv2.imshow('Window1', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()







# import cv2

# cap = cv2.VideoCapture(0)
# # if file path/index is wrong, cap.isOpened() will return false
# while (cap.isOpened()):
#     ret, frame = cap.read()

#     print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

#     cv2.imshow('Window1', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()













import cv2
cap = cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID') # or VideoWriter_fourcc('X', 'V', 'I', 'D')
out1=cv2.VideoWriter('output1.mp4', fourcc, 20, (640, 480)) # 20 fps, 640x480 video size to be saved
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        
        out1.write(frame) # saved the rgb video

        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        cv2.imshow('Window1', gray)
        cv2.imshow('Window2', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

