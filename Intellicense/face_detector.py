# usr/bin/env python3
import numpy as np 
import cv2
import sys

def face_detector(url):
    cascadePath=r'haarcascade_frontalface_alt.xml'
    face_scale= cv2.CascadeClassifier(cascadePath)
    image= cv2.imread(url)
    gray_image= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    array_faces= face_scale.detectMultiScale(gray_image,
                                             scaleFactor=1.2,
                                             minNeighbors=5,
                                             minSize=(10,10))
    
    print("{} Rostros encontrados".format(len(array_faces)))
    for (x,y,w,h) in array_faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Rostros encontrados",image)
    
    if cv2.waitKey(0)& 0xFF==ord('q'):
        return

if __name__=="__main__":
    if len(sys.argv)<2:
        print("Parametros incompletos")
        exit(0)
    #try:
    face_detector(sys.argv[1])
    #except Exception as e:
    #print(e)
        