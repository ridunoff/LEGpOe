from scipy.spatial import distance as dist
import numpy as np
import cv2

def main():


    image = cv2.imread("lego.jpg")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7,7), 0)

    edges = cv2.Canny(gray, 50, 100)
    edges = cv2.dilate(edges, None, iterations=1)
    edges = cv2.erode(edges, None, iterations=1)

    contours = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0]

    reverse = False
    method="left-to-right"
    i = 0

    # handle if we need to sort in reverse
    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True

    # handle if we are sorting against the y-coordinate rather than
    # the x-coordinate of the bounding box
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1

    # construct the list of bounding boxes and sort them from top to
    # bottom
    boundingBoxes = [cv2.boundingRect(c) for c in contours]
    (contours, _) = zip(*sorted(zip(contours, boundingBoxes), key=lambda b: b[1][i], reverse=reverse))

    colors = ((0, 0, 255), (240, 0, 159), (255, 0, 0), (255, 255, 0))

    for (i, c) in enumerate(contours):
	# if the contour is not sufficiently large, ignore it
    	if cv2.contourArea(c) < 100:
    		continue

    	# compute the rotated bounding box of the contour, then
    	# draw the contours
    	box = cv2.minAreaRect(c)
    	box = cv2.cv.BoxPoints(box)
    	box = np.array(box, dtype="int")
    	cv2.drawContours(image, [box], -1, (0, 255, 0), 2)

    	# show the original coordinates
    	print("Object #{}:".format(i + 1))
    	print(box)

        xSorted = box[np.argsort(box[:, 0]), :]

    	# grab the left-most and right-most points from the sorted
    	# x-roodinate points
    	leftMost = xSorted[:2, :]
    	rightMost = xSorted[2:, :]

    	# now, sort the left-most coordinates according to their
    	# y-coordinates so we can grab the top-left and bottom-left
    	# points, respectively
    	leftMost = leftMost[np.argsort(leftMost[:, 1]), :]
    	(tl, bl) = leftMost

    	# now that we have the top-left coordinate, use it as an
    	# anchor to calculate the Euclidean distance between the
    	# top-left and right-most points; by the Pythagorean
    	# theorem, the point with the largest distance will be
    	# our bottom-right point
    	D = dist.cdist(tl[np.newaxis], rightMost, "euclidean")[0]
    	(br, tr) = rightMost[np.argsort(D)[::-1], :]

        rectangle = np.array([tl, tr, br, bl], dtype="float32")

        for ((x, y), color) in zip(rectangle, colors):
		cv2.circle(image, (int(x), int(y)), 5, color, -1)

	# draw the object num at the top-left corner
        cv2.putText(image, "Object #{}".format(i + 1),
		(int(rectangle[0][0] - 15), int(rectangle[0][1] - 15)),
		cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 2)

	# show the image
    	cv2.imshow("Image", image)
    	cv2.waitKey(0)



    cv2.imshow("Image", image)
    cv2.waitKey(0)


if __name__ == "__main__" :
    main()
