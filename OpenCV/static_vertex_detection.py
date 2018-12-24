import numpy as np
import cv2



while(True):
    image = cv2.imread("box.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.bilateralFilter(gray,9,75,75)
    edges = cv2.Canny(blur,100,200)
    dilate = cv2.dilate(edges,None)
    dilate = cv2.bilateralFilter(dilate,9,75,75)
    # gray1 = np.float32(edges)
    dst = cv2.cornerHarris(dilate,2,3,0.04)
    dst = cv2.dilate(dst,None)
    image[dst>0.01*dst.max()]=[0,0,255]


    cv2.imshow("image",image)





    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
