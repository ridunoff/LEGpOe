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









cv2.waitKey()
