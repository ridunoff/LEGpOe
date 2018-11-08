# based off of
# https://learndeltax.blogspot.com/2016/05/3d-object-detection-using-opencv-python.html

import cv2
import numpy as np


def main():
    cap = cv2.VideoCapture(1)
    # current_lego = 0
    i = 0


    while(True):

        ret, frame = cap.read()

        if i % 100 == 0:

            # Image with one lego on tip plate
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
            cv2.namedWindow("Threshold", cv2.WINDOW_NORMAL)
            # show image in the window
            cv2.imshow("Threshold", dilated_image)

            # find the contours
            contours,h = cv2.findContours(dilated_image,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[:2]
            # sorted contours to get largest
            # c = sorted(contours, key=cv2.contourArea, reverse=True)[:1]
            # draw the largest contour
            cv2.drawContours(image, contours, -1, (0,255,0), 3)
            # create window normal size
            cv2.namedWindow("contour", cv2.WINDOW_NORMAL)
            # show image in the window
            cv2.imshow("contour", image)

            # area in contour
            area = cv2.contourArea(contours[0])
            print(area)

        i += 1
        # print(i)






        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__" :
    main()
