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

        ret,frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        min1 = cv2.getTrackbarPos('min', window_name)
        max1 = cv2.getTrackbarPos('max', window_name)

        edges = cv2.Canny(frame,min1,max1)

        cv2.imshow('original', frame)
        cv2.imshow('edges', edges)

        cv2.imshow(window_name,cb)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__" :
    main()


# cap = cv2.VideoCapture(0)
#
# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#
#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Display the resulting frame
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()
