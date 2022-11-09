import numpy as np
import cv2 as cv

#cap = cv.VideoCapture('../../video/avi_sample1.avi')
#cap = cv.VideoCapture('../../video/video1.mp4')
cap = cv.VideoCapture('output.avi')
print('cap.isOpened()', cap.isOpened())
print('size', cap.get(cv.CAP_PROP_FRAME_WIDTH), cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print('fps', cap.get(cv.CAP_PROP_FPS))

while cap.isOpened():
    ret, frame = cap.read()
    print(ret)
    if not ret:
        print("Can't receive frame (stream end?)")
        break

    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()

cv.destroyAllWindows()

