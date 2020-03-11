# /usr/bin/env python3
import numpy as np 
#Broadcasting: forma de disfusion en python
def centrar():
    y= np.random.random(size=(8,9))
    ymean=y.mean(axis=0)
    ycentered= y-ymean
    print(ycentered)
    print(ycentered.mean(axis=0))

if __name__=="__main__":
    centrar()