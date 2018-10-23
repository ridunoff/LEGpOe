import numpy as np
import cv2
# import imutils


cap = cv2.VideoCapture(0)

while(True):

    ret,frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # of red
    lower_red = np.array([0, 110, 110])
    upper_red = np.array([0, 255, 255])

    # of blue
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    res = cv2.bitwise_and(frame,frame, mask=mask_red)


    cv2.imshow('frame', frame)
    cv2.imshow('mask_red', mask_red)
    cv2.imshow('mask_blue', mask_blue)
    cv2.imshow('res', res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
