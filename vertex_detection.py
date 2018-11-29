import cv2
import numpy as np

cap = cv2.VideoCapture(1)

i = 0




## find 4 vertices
# image = cv2.imread("test2_nolight.jpg")
# image = image[0:800, 220:800]

while(True):

    ret, frame = cap.read()

    # if i % 200 == 0:

    frame = frame[50:470, 360:550]




    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    noise_removal = cv2.bilateralFilter(gray,9,75,75)
    ret, threshold_image = cv2.threshold(noise_removal,0,255, cv2.THRESH_OTSU)
    # canny_image = cv2.Canny(threshold_image,250,255)
    # canny_image = cv2.convertScaleAbs(canny_image)
    # kernel = np.ones((3,3),np.uint8)
    # dilated_image = cv2.dilate(canny_image,kernel,iterations=1)
    # contours, h = cv2.findContours(dilated_image,1,2)
    # contours = sorted(contours,key=cv2.contourArea,reverse=True)[:1]
    # cv2.drawContours(image,contours,0,(0,255,0),3)
    corners = cv2.goodFeaturesToTrack(threshold_image,4,0.06,25)
    for item in corners:
        x,y = item[0]
        cv2.circle(frame,(x,y),5,255,-1)

        # cv2.imwrite("i" + str(i) + ".jpg", frame)

    i += 1

    cv2.imshow("threshild", threshold_image)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
