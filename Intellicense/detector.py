# usr/bin/env python3
import cv2
import numpy as np 
import sys 
def detector(url):
    image= cv2.imread(url)
    image_detect=cv2.Canny(image,50,150)
    contorns, hierachy= cv2.findContours(image_detect,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image,contorns,-1,(0,255,0),1)
    cv2.imshow("Contourns found",image)
    print("{} objetos encontrados".format(len(contorns)))
    
if __name__=="__main__":
    if len(sys.argv)<2:
        print("Ingrese una imagen a detectar --<path>")
        exit(0)   
    detector(sys.argv[1])
    cv2.waitKey(0)   
    #print("Hello") 