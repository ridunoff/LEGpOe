import numpy as np
import cv2
from matplotlib import pyplot as plt


def nothing(x):
    pass

def main():

    cap = cv2.VideoCapture(0)

    window_name = 'color range parameter'
    cv2.namedWindow(window_name)

    cb = cv2.imread('lamb.jpg')

    cv2.createTrackbar('min', window_name, 0,500, nothing)
    cv2.createTrackbar('max', window_name, 0,500, nothing)

    while(True):



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

        min1 = cv2.getTrackbarPos('min', window_name)
        max1 = cv2.getTrackbarPos('max', window_name)

        edges = cv2.Canny(gray, min1, max1)
        edges = cv2.dilate(edges, None, iterations=1)
        edges = cv2.erode(edges, None, iterations=1)

        cv2.imshow('frame',edges)
        cv2.imshow(window_name,cb)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__" :
    main()
