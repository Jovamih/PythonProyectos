#! /usr/bin/env python
import numpy as np 

def printList(a,b):
    print("La lista inicial es A={}\nB={}".format(a,b))

def compress(a):
    lista2=[(n+1) for n in a]
    printList(a,lista2)
def numpyCompress(a):
    b=np.array(a)
    b=b/2
    printList(a,b)

    
if __name__ == "__main__":
     lista=[1,2,3,4,5,6,7,32]
     compress(lista)
     numpyCompress(lista)
    