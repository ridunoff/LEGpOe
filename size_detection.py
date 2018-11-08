# based off of
# https://learndeltax.blogspot.com/2016/05/3d-object-detection-using-opencv-python.html

import cv2
import numpy as np

# Image with one lego on tip plate
image = cv2.imread("test2_nolight.jpg")

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
cv2.namedWindow("Dilated", cv2.WINDOW_NORMAL)
# show image in the window
cv2.imshow("Dilated", dilated_image)

# find the contours
contours,h = cv2.findContours(dilated_image,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[:2]
# sorted contours to get largest
c = sorted(contours, key=cv2.contourArea, reverse=True)[:1]
# draw the largest contour
cv2.drawContours(image, c, -1, (0,255,0), 3)
# create window normal size
cv2.namedWindow("Contour", cv2.WINDOW_NORMAL)
# show image in the window
cv2.imshow("Contour", image)

# area in contour
area = cv2.contourArea(c[0])



cv2.waitKey()
