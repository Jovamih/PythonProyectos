# usr/bin/env python3
import cv2
import numpy as np 
import sys
from os import path

def face_advanced(video):
    scalePath=r"c:/user/Projects/PythonPoyectos/Intellicense/haarcascade_frontalface_alt.xml"
    print(scalePath)
    face_scale= cv2.CascadeClassifier(scalePath)
    
    while video.isOpened():
        ret,image=video.read()
        if not ret:
            break
        image_gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        
        array_faces=face_scale.detectMultiScale(
            image_gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(2,2)
        )
        for (x,y,w,h) in array_faces:
                cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
       
        cv2.imshow("Face detector",image)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
        
    video.release()
    cv2.destroyAllWindows()
        
        
if __name__=="__main__":
    if len(sys.argv)<2:
        video=cv2.VideoCapture(0,cv2.CAP_DSHOW)
    else:
        video=cv2.VideoCapture(sys.argv[1])
    try:
        face_advanced(video)
    except Exception as e:
        print(e,file=sys.stderr)
        