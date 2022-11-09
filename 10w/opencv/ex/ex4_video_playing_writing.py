import numpy as np
import cv2 as cv

cap = cv.VideoCapture('../../video/avi_sample1.avi')
#cap = cv.VideoCapture(0)
#cap = cv.VideoCapture('../../video/video1.mp4')
print('cap.isOpened()', cap.isOpened())
print('size', cap.get(cv.CAP_PROP_FRAME_WIDTH), cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print('fps', cap.get(cv.CAP_PROP_FPS))

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, cap.get(cv.CAP_PROP_FPS), (320, 240))

while cap.isOpened():
    ret, frame = cap.read()
    print(ret)
    if not ret:
        print("Can't receive frame (stream end?)")
        break
    #frame = cv.resize(frame, dsize=(0,0), fx=0.5, fy=0.5)
    frame = cv.resize(frame, dsize=(320,240))
    out.write(frame)
    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()

