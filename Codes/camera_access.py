import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#cap.set(cv2.CV_CAP_PROP_FRAME_WIDTH, 640)
#cap.set(cv2.CV_CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    cv2.imshow('preview',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
