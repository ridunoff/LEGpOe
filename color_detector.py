import numpy as np
import cv2
# import imutils



def main():
    cap = cv2.VideoCapture(0)
    current_lego = []

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

            c = max(contours_red, key=cv2.contourArea)
            ((x,y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            red_center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255), 2)
            cv2.circle(frame, red_center, 5, (0, 0, 255), -1)
            red_coordinates.append(red_center[1])
            if "red" != current_lego[0]:
                current_lego[0] = "red"
                print("red")



        elif len(contours_blue) > 0:
            c = max(contours_blue, key=cv2.contourArea)
            ((x,y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            blue_center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255), 2)
            cv2.circle(frame, blue_center, 5, (0, 0, 255), -1)
            blue_coordinates.append(blue_center[1])
            if "blue" != current_lego[0]:
                current_lego[0] = "blue"
                print("blue")
        elif len(contours_green) > 0:
            c = max(contours_green, key=cv2.contourArea)
            ((x,y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            green_center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255), 2)
            cv2.circle(frame, green_center, 5, (0, 0, 255), -1)
            green_coordinates.append(green_center[1])
            if "grenn" != current_lego[0]:
                current_lego[0] = "green"
                print("grenn")
        elif len(contours_yellow) > 0:
            c = max(contours_yellow, key=cv2.contourArea)
            ((x,y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            red_center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255), 2)
            cv2.circle(frame, yellow_center, 5, (0, 0, 255), -1)
            red_coordinates.append(yellow_center[1])
            if "yellow" != current_lego[0]:
                current_lego[0] = "yellow"
                print("yellow")
        else:
            print(" ")






        # res_red = cv2.bitwise_and(frame,frame, mask=mask_red)
        res_blue = cv2.bitwise_and(frame,frame, mask=mask_blue)
        # res_green = cv2.bitwise_and(frame,frame, mask=mask_green)
        # res_yellow = cv2.bitwise_and(frame,frame, mask=mask_yellow)


        cv2.imshow('frame', frame)
        # cv2.imshow('mask_red', mask_red)
        cv2.imshow('mask_blue', mask_blue)
        # cv2.imshow('res_red', res_red)
        cv2.imshow('res_blue', res_blue)
        # cv2.imshow('res_green', res_green)
        # cv2.imshow('res_yellow', res_yellow)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__" :
    main()
