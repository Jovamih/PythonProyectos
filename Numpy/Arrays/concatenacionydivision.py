# /usr/bin/env python
import numpy as np 

def concatenar():
    np.random.seed(0)
    x0=np.random.randint(10,size=(2,7))
    y0=np.random.randint(70,size=(3,7))
    z0= np.concatenate([x0,y0])
    print("Concatenado")
    print(z0)
    print("concatenado -> np.vstack() de forma vertical")
    z0= np.vstack([y0,x0])
    print(z0)
    x0=x0.reshape((7,2))
    y0=y0.reshape((7,3))
    z0=np.hstack([y0,x0])
    print("Concatenado -> np.hstack() de forma horizontal")
    print(z0)
    
def dividirArray():
    pass

if __name__=="__main__":
    concatenar()
    
    
     