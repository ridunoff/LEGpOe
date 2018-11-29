# based off of
# https://learndeltax.blogspot.com/2016/05/3d-object-detection-using-opencv-python.html

import cv2
import numpy as np
import time
# import serial

baudRate = 9600
# arduinoComPort = "/dev/ttyACM0"
# serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)


def create_limits(low1,low2,low3,high1,high2,high3):

    lower_limit = np.array([low1,low2,low3])
    upper_limit = np.array([high1,high2,high3])

    return lower_limit,upper_limit


def create_mask(hsv,lower_limit,upper_limit):
    mask = cv2.inRange(hsv,lower_limit,upper_limit)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    return mask

def find_contours(mask):
    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    coordinates = []

    return contours, center, coordinates

def main():
    # cap = cv2.VideoCapture(1)
    # current_lego = 0
    i = 0
    write_code = 0


    while(True):

        # ret, frame = cap.read()
        frame = cv2.imread("/home/anna/LEGpOe/test2_nolight.jpg")

        blurred_frame = cv2.GaussianBlur(frame.copy(), (5,5), 0)
        hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)


        # CHANGED created fuction for limits
        # of red
        lower_red, upper_red = create_limits(0, 110, 110, 10, 255, 255)
        # of blue
        lower_blue, upper_blue = create_limits(85, 27, 46, 165, 168, 77)
        # of green
        lower_green, upper_green = create_limits(30, 50, 0, 100, 255, 150)
        # of yellow
        lower_yellow, upper_yellow = create_limits(0, 80, 70, 255, 255, 255)


        # CHANGED created function for masks
        mask_red = create_mask(hsv,lower_red,upper_red)
        mask_blue = create_mask(hsv,lower_blue,upper_blue)
        mask_green = create_mask(hsv,lower_green,upper_green)
        mask_yellow = create_mask(hsv,lower_yellow,upper_yellow)

        if i % 200 == 0:

            # Image with one lego on tip plate
                # y and then x
            image = frame

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
            print(area)


            if area > 2500 and area < 4000:
                write_code = write_code + 2
            elif area > 26000 and area < 30000:
                write_code = write_code + 4


            # CHANGED made fucton to find contours
            contours_red, red_center, red_coordinates = find_contours(mask_red)
            contours_blue, blue_center, blue_coordinates = find_contours(mask_blue)
            contours_green, green_center, green_coordinates = find_contours(mask_green)
            contours_yellow, yellow_center, yellow_coordinates = find_contours(mask_yellow)

            if len(contours_red) > 0:

                # CHANGED delete unnecessary
                # c = max(contours_red, key=cv2.contourArea)
                # ((x,y), radius) = cv2.minEnclosingCircle(c)
                # M = cv2.moments(c)
                # red_center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                # cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255), 2)
                # cv2.circle(frame, red_center, 5, (0, 0, 255), -1)
                # red_coordinates.append(red_center[1])

                    # print("red")
                write_code = write_code + 10



            elif len(contours_blue) > 0:
                print("got here")
                # c = max(contours_blue, key=cv2.contourArea)
                # ((x,y), radius) = cv2.minEnclosingCircle(c)
                # M = cv2.moments(c)
                # blue_center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                # cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255), 2)
                # cv2.circle(frame, blue_center, 5, (0, 0, 255), -1)
                # blue_coordinates.append(blue_center[1])
                print("blue")


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




        if write_code == 4:
            # serialPort.write("4")
            print("Blue 2x4")
        elif write_code == 2:
            # serialPort.write("2")
            print("Blue 2x2")
        elif write_code == 14:
            # serialPort.write("14")
            print("Red 2x4")
        elif write_code == 12:
            # serialPort.write("12")
            print("Red 2x2")
        i += 1
        write_code = 0
        # print(i)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__" :
    main()
