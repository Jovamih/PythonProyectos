# /usr/bin/env python3
import numpy as np 
#Indexacio x[:]
def index():
    np.random.seed(0)
    x=np.random.randint(0,10,size=(3,4))
    print(x)
    for l in range((x.shape)[0]):
        for j in range((x.shape)[1]):
            print(x[l][j],end=' ')
        print()
    #Acceso a SubArreglos
    #X[start:stop=size:step]
    y=np.arange(10)
    print(y[2:4])
    print(y[::2])
    print(y[0:8:3])
    #Acceso a subarrelos dimensionales
    #Y[:,:]
    Y=np.random.randint(0,20,size=(5,5))
    print(Y)
    print(Y[:3,:3])
    Y_copy=Y[2:,3:].copy()
    print("SUBCOPIA")
    print(Y_copy)
    
if __name__=="__main__":
    index()
        