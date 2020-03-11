# usr/bin/env python3
import cv2
import sys

def show_image(url):
    image=cv2.imread(url)
    cv2.imshow("Process Image",image)
    #cv2.waitKey(0)
def show_scaled(url):
    image=cv2.imread(url)
    gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Imagen en gris",gray_image)
    #cv2.waitKey(0)
def show_gaussian(url):
    image=cv2.imread(url)
    gauss= cv2.GaussianBlur(image,(7,7),0)
    cv2.imshow("Difuminacion gaussiana",gauss)
    
def show_detectorCanny(url):
    image=cv2.imread(url)
    detector= cv2.Canny(image,50,150)
    cv2.imshow("Detector",detector)
def show_detectorAdvanced(url):
    image=cv2.imread(url)
    im_scale= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    im_canny= cv2.Canny(im_scale,50,150)
    cv2.imshow("Canny advanced",im_canny)

if __name__=="__main__":
    if len(sys.argv)<2:
        print("Ingrese la ruta de la imagen --<image>")
        exit(0)
    try:
        #show_image(sys.argv[1])
        #show_scaled(sys.argv[1])
        #show_gaussian(sys.argv[1])
        #show_detectorCanny(sys.argv[1])
        show_detectorAdvanced(sys.argv[1])
        cv2.waitKey(0)
    except Exception as e:
        print(e)
        