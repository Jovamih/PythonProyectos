# /usr/bin/env python
import numpy as np 
#funciones universales

def ufuncs(ar):
    x=np.empty(len(ar))
    for i in range(len(ar)):
        x[i]=1.0/ar[i]
    return x
def operaciones(ar):
    x=np.array([ 1.0/l for l in ar])
    # o tambien se puede hacer lo siguiente
    ar=1.0/ar
    print(ar)
    print(ar+2)
    print(ar-4)
    print(ar*5)
    print(ar/6)
    print(ar//2)
    print(ar%4)
    print(ar**5)
if __name__=="__main__":
    ar=np.random.randint(1,40,size=20)
    operaciones(ar)