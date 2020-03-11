# /usr/bin/env python3
import numpy as np 

def otros():
    x=np.random.randint(10,size=8)
    y=np.empty(8)
    np.multiply(x,2, out=y)
    print(y)
def agregados():
    #reduce y acumulate
    x=np.random.randint(9,23,size=20)
    z=np.arange(1,4)
    print(x)
    print(np.add.reduce(x))
    print(np.add.accumulate(x))
    #funciones externas
    f= np.multiply.outer(x,z)
    print(f)

if __name__=="__main__":
    agregados()