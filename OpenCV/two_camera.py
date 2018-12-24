#https://www.codesofinterest.com/2018/09/using-multiple-cameras-with-opencv.html

import numpy as np
import cv2
import time
import serial

baudRate = 9600
arduinoComPort = "/dev/ttyACM0"
serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)

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

    # 0 for computer camera, 1 for external camera
    cap1 = cv2.VideoCapture(1)
    cap2 = cv2.VideoCapture(2)
    write_code = 0
    i = 0




    while(True):
        # Capture frame-by-frame
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        frame1 = frame1[170:350,250:520]
        frame2 = frame2[200:400,100:400]



        blurred_frame = cv2.GaussianBlur(frame1.copy(), (5,5), 0)
        hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)


        # of red
        lower_red, upper_red = create_limits(0, 130, 155, 221, 193, 255)

        # of blue
        lower_blue, upper_blue = create_limits(80, 125, 80, 240, 255, 143)

        # of green
        lower_green, upper_green = create_limits(45, 125, 0, 150, 255, 150)

        mask_red = create_mask(hsv,lower_red,upper_red)
        mask_blue = create_mask(hsv,lower_blue,upper_blue)
        mask_green = create_mask(hsv,lower_green,upper_green)

        if i % 200 == 0:

            image1 = frame1
            image2 = frame2


            gray1 = cv2.cvtColor(image1, cv2.COLOR_RGB2GRAY)
            gray2 = cv2.cvtColor(image2, cv2.COLOR_RGB2GRAY)

            refined_image1 = cv2.bilateralFilter(gray1,9,75,75)
            refined_image2 = cv2.bilateralFilter(gray2,9,75,75)

            ret1, threshold_image1 = cv2.threshold(refined_image1,0,255,cv2.THRESH_OTSU)
            ret2, threshold_image2 = cv2.threshold(refined_image2,0,255,cv2.THRESH_OTSU)

            canny1 = cv2.Canny(threshold_image1, 250, 255)
            canny2 = cv2.Canny(threshold_image2, 250, 255)

            kernel = np.ones((3,3), np.uint8)
            dilated_image1 = cv2.dilate(canny1,kernel, iterations=1)
            dilated_image2 = cv2.dilate(canny2,kernel, iterations=1)

            contours1,h1 = cv2.findContours(dilated_image1,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[:2]
            contours2,h2 = cv2.findContours(dilated_image2,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[:2]



            c1 = sorted(contours1, key=cv2.contourArea, reverse=True)[:1]
            c2 = sorted(contours2, key=cv2.contourArea, reverse=True)[:1]


            # cv2.drawContours(image1, c1, 0, (0,255,0), 3)
            # cv2.drawContours(image2, c2, 0, (255,0,0), 3)

            x1,y1,w1,h1 = cv2.boundingRect(c1[0])
            cv2.rectangle(image1,(x1,y1),(x1+w1,y1+h1), (0,255,0),3)

            x2,y2,w2,h2 = cv2.boundingRect(c2[0])
            cv2.rectangle(image2,(x2,y2),(x2+w2,y2+h2), (255,0,0),3)

            rect1 = cv2.minAreaRect(c1[0])
            box1 = cv2.cv.BoxPoints(rect1)
            box1 = np.int0(box1)
            cv2.drawContours(image1,[box1],0,(0,255,0),3)

            rect2 = cv2.minAreaRect(c2[0])
            box2 = cv2.cv.BoxPoints(rect2)
            box2 = np.int0(box2)
            cv2.drawContours(image2,[box2],0,(255,0,0),3)

            summ = cv2.contourArea(box1) + cv2.contourArea(box2)
            print(summ)

            if summ < 10000:
                write_code += 1
            elif summ > 10000 and summ < 11000:
                write_code += 3
            elif summ > 13000:
                write_code += 2


            contours_red, red_center, red_coordinates = find_contours(mask_red)
            contours_blue, blue_center, blue_coordinates = find_contours(mask_blue)
            contours_green, green_center, green_coordinates = find_contours(mask_green)

            if len(contours_red) > 0:
                write_code = write_code + 10

            elif len(contours_blue) > 0:
                # unnecessary
                write_code = write_code + 20
            elif len(contours_green) > 0:
                write_code = write_code + 30


            if write_code == 21:
                print("Blue 2x2")
                serialPort.write("20")
            elif write_code == 22:
                print(" Blue 2x4")
                serialPort.write("40")
            elif write_code == 23:
                print(" Blue 1x4")
                serialPort.write("60")
            elif write_code == 11:
                print("Red 2x2")
                serialPort.write("80")
            elif write_code == 12:
                print("Red 2x4")
                serialPort.write("100")
            elif write_code == 13:
                print(" Red 1x4")
                serialPort.write("120")
            elif write_code == 31:
                print("Green 2x2")
                serialPort.write("140")
            elif write_code == 32:
                print("Green 2x4")
                serialPort.write("160")
            elif write_code == 33:
                print("Green 1x4")
                serialPort.write("180")
            else:
                print("Unknown")
                serialPort.write("0")

        i += 1
        # print(write_code)
        write_code = 0






        if ret1:
            cv2.imshow('Cam1',image1)

        if ret2:
            cv2.imshow("Cam2", image2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()


if __name__ == "__main__" :
    main()
