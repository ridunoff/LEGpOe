import numpy as np
import cv2
# import imutils

def main():
    cap = cv2.VideoCapture(0)

    while(True):

        ret,frame = cap.read()
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
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
        lower_yellow = np.array([10, 200, 150])
        upper_yellow = np.array([255, 255, 255])


        mask_red = cv2.inRange(hsv, lower_red, upper_red)
        # mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        # mask_green = cv2.inRange(hsv, lower_green, upper_green)
        # mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

        contours, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for each in contours:
            area = cv2.contourArea(each)
            # frame, contours, all of them, (green), thikness=3
            if area > 1000:
                cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)



        res_red = cv2.bitwise_and(frame,frame, mask=mask_red)
        # res_blue = cv2.bitwise_and(frame,frame, mask=mask_blue)
        # res_green = cv2.bitwise_and(frame,frame, mask=mask_green)
        # res_yellow = cv2.bitwise_and(frame,frame, mask=mask_yellow)


        cv2.imshow('frame', frame)
        # cv2.imshow('mask_red', mask_red)
        # cv2.imshow('mask_blue', mask_blue)
        cv2.imshow('res_red', res_red)
        # cv2.imshow('res_blue', res_blue)
        # cv2.imshow('res_green', res_green)
        # cv2.imshow('res_yellow', res_yellow)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__" :
    main()
