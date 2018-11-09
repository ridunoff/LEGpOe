# based off of
# https://learndeltax.blogspot.com/2016/05/3d-object-detection-using-opencv-python.html

import cv2
import numpy as np
import time
import serial

baudRate = 9600
arduinoComPort = "/dev/ttyACM0"
serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)


def main():
    cap = cv2.VideoCapture(1)
    # current_lego = 0
    i = 0
    write_code = 0
    current_lego = 0


    while(True):

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

        if i % 200 == 0:

            # Image with one lego on tip plate
                # y and then x
            image = frame[50:460, 240:450]



            # create window normal size
            cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
            # show image in the window
            cv2.imshow("Original", image)


            # convert to grayscale
            gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
            # create window normal size
            cv2.namedWindow("Grayscale", cv2.WINDOW_NORMAL)
            # show image in the window
            cv2.imshow("Grayscale", gray)

            # noise removal but keeps edges
            # this filter is slower than most but it is very good at preserving edges
            refined_image = cv2.bilateralFilter(gray,9,75,75)
            # thresholding using THRESH_OTSU
            # needs a bimodal image and finds a threshold inbetween the two peaks
            # pixels are set to either black or wight depending on how they compare to the threshold
            ret, threshold_image = cv2.threshold(refined_image,0,255,cv2.THRESH_OTSU)
            # create window normal size
            cv2.namedWindow("Threshold", cv2.WINDOW_NORMAL)
            # show image in the window
            cv2.imshow("Threshold", threshold_image)


            # Canny Edge detection
            canny_edge_detection = cv2.Canny(threshold_image, 250, 255)
            # kernal for dilation, 3x3
            kernel = np.ones((3,3), np.uint8)
            dilated_image = cv2.dilate(canny_edge_detection,kernel, iterations=1)
            # create window normal size
            cv2.namedWindow("Edges", cv2.WINDOW_NORMAL)
            # show image in the window
            cv2.imshow("Edges", dilated_image)

            # find the contours
            contours,h = cv2.findContours(dilated_image,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[:2]
            # sorted contours to get largest
            c = sorted(contours, key=cv2.contourArea, reverse=True)[:1]
            print(len(c))
            # draw the largest contour
            cv2.drawContours(image, c, 0, (0,255,0), 3)
            # cv2.drawContours(image, c, 1, (0,0,255), 3)
            # create window normal size
            cv2.namedWindow("contour", cv2.WINDOW_NORMAL)
            # show image in the window
            cv2.imshow("contour", image)

            # area in contour
            area = cv2.contourArea(c[0])

            if area > 2500 and area < 4000:
                write_code = write_code + 2
            elif area > 5500 and area < 7000:
                write_code = write_code + 4

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
                if current_lego != 1:
                    current_lego = 1
                    # print("red")
                    write_code = write_code + 10



            elif len(contours_blue) > 0:
                c = max(contours_blue, key=cv2.contourArea)
                ((x,y), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                blue_center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255), 2)
                cv2.circle(frame, blue_center, 5, (0, 0, 255), -1)
                blue_coordinates.append(blue_center[1])
                if current_lego != 2:
                    current_lego = 2
                    # print("blue")


            # elif len(contours_green) > 0:
            #     c = max(contours_green, key=cv2.contourArea)
            #     ((x,y), radius) = cv2.minEnclosingCircle(c)
            #     M = cv2.moments(c)
            #     green_center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            #     cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255), 2)
            #     cv2.circle(frame, green_center, 5, (0, 0, 255), -1)
            #     green_coordinates.append(green_center[1])
            #     if current_lego != 3:
            #         current_lego = 3
            #         print("green")
            #
            #
            # elif len(contours_yellow) > 0:
            #     c = max(contours_yellow, key=cv2.contourArea)
            #     ((x,y), radius) = cv2.minEnclosingCircle(c)
            #     M = cv2.moments(c)
            #     yellow_center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            #     cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255), 2)
            #     cv2.circle(frame, yellow_center, 5, (0, 0, 255), -1)
            #     red_coordinates.append(yellow_center[1])
            #     if current_lego != 4:
            #         current_lego = 4
            #         print("yellow")

            current_lego = 0



        if write_code == 4:
            serialPort.write("4")
            print("Blue 2x4")
        elif write_code == 2:
            serialPort.write("2")
            print("Blue 2x2")
        elif write_code == 14:
            serialPort.write("14")
            print("Red 2x4")
        elif write_code == 12:
            serialPort.write("12")
            print("Red 2x2")
        i += 1
        write_code = 0
        # print(i)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__" :
    main()
