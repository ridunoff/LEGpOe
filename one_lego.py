

import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    blurred_frame = cv2.GaussianBlur(frame.copy(), (5,5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)


    # of red
    lower_red = np.array([0, 110, 110])
    upper_red = np.array([10, 255, 255])

    # of blue
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # of green
    lower_green = np.array([30, 50, 0])
    upper_green = np.array([100, 255, 150])

    # of yellow
    lower_yellow = np.array([0, 80, 70])
    upper_yellow = np.array([255, 255, 255])


    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_red = cv2.erode(mask_red, None, iterations=2)
    mask_red = cv2.dilate(mask_red, None, iterations=2)

    # blue mask, binary, reduce noise
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_blue = cv2.erode(mask_blue, None, iterations=2)
    mask_blue = cv2.dilate(mask_blue, None, iterations=2)

    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_green = cv2.erode(mask_green, None, iterations=2)
    mask_green = cv2.dilate(mask_green, None, iterations=2)

    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask_yellow = cv2.erode(mask_yellow, None, iterations=2)
    mask_yellow = cv2.dilate(mask_yellow, None, iterations=2)

    contours_red = cv2.findContours(mask_red.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    red_center = None
    red_coordinates = []

    contours_blue = cv2.findContours(mask_blue.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    blue_center = None
    blue_coordinates = []

    contours_green = cv2.findContours(mask_green.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    green_center = None
    green_coordinates = []

    contours_yellow = cv2.findContours(mask_yellow.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    yellow_center = None
    yellow_coordinates = []

    if len(contours_red) > 0:
        res_red = cv2.bitwise_and(frame,frame, mask=mask_red)
        gray = cv2.cvtColor(res_red, cv2.COLOR_HSV2BGR)
        gray = cv2.cvtColor(res_red, cv2.COLOR_BGR2GRAY)
        mask = mask_red

    elif len(contours_blue) > 0:
        res_blue = cv2.bitwise_and(frame,frame, mask=mask_blue)
        gray = cv2.cvtColor(res_blue, cv2.COLOR_HSV2BGR)
        gray = cv2.cvtColor(res_blue, cv2.COLOR_BGR2GRAY)
        mask = mask_blue

    elif len(contours_green) > 0:
        res_green = cv2.bitwise_and(frame,frame, mask=mask_green)
        gray = cv2.cvtColor(res_green, cv2.COLOR_HSV2BGR)
        gray = cv2.cvtColor(res_green, cv2.COLOR_BGR2GRAY)
        mask = mask_green

    elif len(contours_yellow) > 0:
        res_yellow = cv2.bitwise_and(frame,frame, mask=mask_yellow)
        gray = cv2.cvtColor(res_yellow, cv2.COLOR_HSV2BGR)
        gray = cv2.cvtColor(res_yellow, cv2.COLOR_BGR2GRAY)
        mask = mask_yellow

    edges = cv2.Canny(gray, 50, 100)
    edges = cv2.dilate(edges, None, iterations=1)
    edges = cv2.erode(edges, None, iterations=1)

    # contours_blue = cv2.findContours(mask_blue.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    # blue_center = None
    # blue_coordinates = []
    # cv2.drawContours(frame, contours_blue, -1, (0,255,0), 3)

    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    coordinates = []
    cv2.drawContours(frame, contours, -1, (0,255,0), 3)

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
    cv2.imshow('test', mask)
    cv2.imshow('frame2', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
