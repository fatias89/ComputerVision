import numpy as np
import cv2

def get_limits (color):
    c=np.uint8([[color]])
    hsvC=cv2.cvtColor(c,cv2.COLOR_BGR2HSV)
    lowerLimit=hsvC[0][0][0]- 10,100,100
    uppererLimit = hsvC[0][0][0] + 10, 255, 255

    lowerLimit=np.array(lowerLimit,dtype=np.uint8)
    uppererLimit = np.array(uppererLimit, dtype=np.uint8)

    return lowerLimit,uppererLimit