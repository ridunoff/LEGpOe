import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    blurred_frame = cv2.GaussianBlur(frame.copy(), (5,5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)


    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])


    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_blue = cv2.erode(mask_blue, None, iterations=2)
    mask_blue = cv2.dilate(mask_blue, None, iterations=2)

    res_blue = cv2.bitwise_and(frame,frame, mask=mask_blue)
    gray = cv2.cvtColor(res_blue, cv2.COLOR_HSV2BGR)
    gray = cv2.cvtColor(res_blue, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 62, 25)
    edges = cv2.dilate(edges, None, iterations=1)
    edges = cv2.erode(edges, None, iterations=1)

    contours_blue = cv2.findContours(mask_blue.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    blue_center = None
    blue_coordinates = []
    cv2.drawContours(frame, contours_blue, -1, (0,255,0), 3)

    # if len(contours_blue) > 0:


        # c = max(contours_blue, key=cv2.contourArea)
        # ((x,y), radius) = cv2.minEnclosingCircle(c)
        # M = cv2.moments(c)
        # blue_center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        # cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255), 2)
        # cv2.circle(frame, blue_center, 5, (0, 0, 255), -1)
        # blue_coordinates.append(blue_center[1])









    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray = cv2.GaussianBlur(gray, (7,7), 0)
    #
    # edges = cv2.Canny(gray, 50, 175)
    # edges = cv2.dilate(edges, None, iterations=1)
    # edges = cv2.erode(edges, None, iterations=1)

    # Display the resulting frame
    cv2.imshow('frame',edges)
    cv2.imshow('test', mask_blue)
    cv2.imshow('frame2', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
