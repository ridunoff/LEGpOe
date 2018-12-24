import cv2
import numpy as np

# Sliders to determine upper and lower linmits


def nothing(x):
    pass

def main():

    # cap = cv2.VideoCapture(0)

    window_name = 'color range parameter'
    cv2.namedWindow(window_name)

    cb = cv2.imread('lamb.jpg')

    # hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    cv2.createTrackbar('a1',window_name,0,255,nothing)
    cv2.createTrackbar('a2',window_name,0,255,nothing)
    cv2.createTrackbar('a3',window_name,0,255,nothing)

    cv2.createTrackbar('b1',window_name,150,255,nothing)
    cv2.createTrackbar('b2',window_name,150,255,nothing)
    cv2.createTrackbar('b3',window_name,150,255,nothing)

    while(True):

        # ret,frame = cap.read()
        frame = cv2.imread("/home/anna/LEGpOe/black.jpg")
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        a1 = cv2.getTrackbarPos('a1',window_name)
        a2 = cv2.getTrackbarPos('a2',window_name)
        a3 = cv2.getTrackbarPos('a3',window_name)

        b1 = cv2.getTrackbarPos('b1',window_name)
        b2 = cv2.getTrackbarPos('b2',window_name)
        b3 = cv2.getTrackbarPos('b3',window_name)

        lower = np.array([a1,a2,a3])
        upper = np.array([b1,b2,b3])
        mask = cv2.inRange(hsv, lower, upper)
        res = cv2.bitwise_and(frame,frame,mask=mask)

        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        cv2.imshow('frame',frame)
        cv2.imshow(window_name,cb)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__" :
    main()
