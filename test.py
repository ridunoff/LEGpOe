
import numpy as np
import cv2
from scipy.spatial import distance as dist


def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)


def main():


    image = cv2.imread("coffee.jpg")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7,7), 0)

    edges = cv2.Canny(gray, 50, 100)
    edges = cv2.dilate(edges, None, iterations=1)
    edges = cv2.erode(edges, None, iterations=1)

    contours = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    coutours = contours[1]

    reverse = False
    i = 0

    boundingBoxes = [cv2.boundingRect(c) for c in countours]
    (countours, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b: b[1][i], reverse=reverse))


    for each in countours:
        if cv2.countourArea(each) < 100:
            continue


        original = image.copy()
        box = cv2.minAreaRect(each)
        box = cv2.cv.BoxPoints(box)
        box = np.array(box, dtype="int")

        xSorted = box[np.arsort(box[:,0]),:]

        leftMost = xSorted[:2,:]
        rightMost = xSorted[2:,:]

        leftMost = leftMost[np.argsort(leftMost[:, 1]), :]
        (t1,b1) = leftMost

        D = dist.cdist(t1[np.newaxis], rightMost, "euclidean")[0]
        (br, tr) = rightMost[np.argsort(D)[::-1],:]

        box = np.array([t1,tr,br,b1], dtype="float32")
        cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)

        for (x, y) in box:
			cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)

		(tl, tr, br, bl) = box
		(tltrX, tltrY) = midpoint(tl, tr)
		(blbrX, blbrY) = midpoint(bl, br)
        (tlblX, tlblY) = midpoint(tl, bl)
		(trbrX, trbrY) = midpoint(tr, br)

        cv2.circle(original, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
    	cv2.circle(origianl, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
    	cv2.circle(original, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
    	cv2.circle(original, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)

        cv2.line(original, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
		(255, 0, 255), 2)
	    cv2.line(original, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
		(255, 0, 255), 2)

        dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
	    dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

        pixelsPerMetric = dB / 157

        dimA = dA / pixelsPerMetric
	    dimB = dB / pixelsPerMetric

        cv2.imshow("Image", orig)
	    cv2.waitKey(0)


if __name__ == "__main__" :
    main()
