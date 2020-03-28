#/usr/bin/env python3

import cv2
import sys
def identifier(path):
    cascadePath=r"D:\User\PythonProyectos\Intellicense\haarcascade_frontalface_alt.xml"
    detector=cv2.CascadeClassifier(cascadePath)
    image=cv2.imread(path)
    image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #ubicamos las caras en la imagen
    array_faces=detector.detectMultiScale(
        image_gray,
        scaleFactor=1.2,
        minNeighbors=2,
        minSize=(1,1)
    )
    #dibujamos las caras en la imagen segun sean las cordenadas encontradas
    for (x,y,w,h) in array_faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    
    print("{} rostros encontrados".format(len(array_faces)))
    #mostramos la imagen
    cv2.imshow("{} Faces found".format(len(array_faces)),image)
    if cv2.waitKey(0) & 0xFF==ord('q'):
        return

if __name__=="__main__":
    
    if len(sys.argv)<2:
        print("Debe especifica una imagen como ruta de acceso")
        exit(0)
    try:
        identifier(sys.argv[1])
    except Exception as e:
        print(e)