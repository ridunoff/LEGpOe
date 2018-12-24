## https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html

import numpy as np
import cv2


def nothing(x):
    pass



def main():
# 0 for computer camera, 1 for externalcap = cv2.VideoCapture(1)

    cap = cv2.VideoCapture(1)




    while(True):
        # Capture frame-by-frame


        ret, frame = cap.read()
        # frame = frame[158:370,100:410]
        frame = frame[85:380,100:500]


        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__" :
    main()
