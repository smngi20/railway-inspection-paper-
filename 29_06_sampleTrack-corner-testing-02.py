#CORNER DETECTION 


import cv2
import numpy as np
from matplotlib import pyplot as plt

#cv2.namedWindow("res")
frame = cv2.imread("sampletrack.png")




gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray1',gray)

#gray = np.float32(gray) - idk why this 

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
#corners = np.int0(corners)

print(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(frame,(x,y),3,255,-1)

cv2.imshow('res',frame)

key = cv2.waitKey(100000)

# cv2.destroyWindow("Webcam Feed")
#
#cv2.destroyAllWindows()