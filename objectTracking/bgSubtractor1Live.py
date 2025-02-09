import numpy as np
import cv2

cap = cv2.VideoCapture(0)

foreground_background = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    
    ret, frame = cap.read()
    
    frame = cv2.flip(frame, 1)

    foreground_mask = foreground_background.apply(frame)

    cv2.imshow('Output', foreground_mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()