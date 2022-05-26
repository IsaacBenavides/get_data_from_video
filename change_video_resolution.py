import cv2
import numpy as np
import sys

try:

    cap = cv2.VideoCapture(sys.argv[1])

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(f"resized_video.avi", fourcc, 5, (320, 240))

    while True:
        ret, frame = cap.read()
        if ret == True:
            b = cv2.resize(frame, (320, 240), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
            out.write(b)
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

except:
    print("Usage: \n - python change_video_resolution.py [path for video]")
