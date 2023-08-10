import cv2
from util import get_limits

from PIL import Image
cap=cv2.VideoCapture(0)
yellow=[255,0,0]
while True:
    ret,frame=cap.read()
    hsvImage=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerLimit, uppererLimit=get_limits(yellow)
    mask=cv2.inRange(hsvImage,lowerLimit, uppererLimit)
    masknumpy=Image.fromarray(mask)
    bbox=masknumpy.getbbox()
    if bbox is not None:
        x1,y1,x2,y2=bbox
        frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1)==ord('q'):
         break
cap.release()
cv2.destroyAllWindows()