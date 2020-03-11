# usr/bin/env python
import cv2
import numpy as np 
import sys

def motion_detector(video):
    
    while video.isOpened():
        ret,image_last=video.read()
        ret,image_current=video.read()
        if not ret:
            break
        diff= cv2.absdiff(image_last,image_current)
        if np.mean(diff)>3:
            print("Movimiento detectado :{}".format(np.mean(diff)))
        cv2.imshow("Motion Dectector",image_current)
        if cv2.waitKey(1) & 0xFF==ord('q'):
             break



if __name__=="__main__":
    if len(sys.argv)<2:
        video=cv2.VideoCapture(0)
    else:
        video=cv2.VideoCapture(sys.argv[1])
      
    try:  
        motion_detector(video)
        video.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(e)