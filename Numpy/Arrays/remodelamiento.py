# /usr/bin/env python3
import numpy as np 

#funcion reshape()
#funcion np.newaxis
def reshape():
    print("matriz en ejecucion")
    x= np.arange(20).reshape((4,5))
    print(x)
    print("Matriz ya creada")
    x=x.reshape((2,10))
    print(x)
    #x=x[:,np.newaxis]
    #x=x[np.newaxis,:]
    
    
if __name__=="__main__":
    reshape()
    