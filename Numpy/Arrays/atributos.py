# /usr/bin/env python3
import numpy as np 
import sys

def atributos():
    np.random.seed(0)
    x1= np.random.randint(2,10,size=6)
    x2=np.random.randint(2,10,size=(3,5))
    x3=np.random.randint(2,10,size=(3,4,5))
   #ndim= Numero de dimesiones
   #shape=Retorna el tamaño de las dimensiones (a,b)
   #size= El tamaño de las dimensiones (n de elementos)
   #dtype= tipo de elemento
   #itemsize=El tamaño de cada elemnto de la matriz
   #nbytes El tamaño total de la matriz en byte's
    print(x3.ndim)
    print(x3.shape)
    print(x3.size)
    print(x3.itemsize,x3.nbytes)

if __name__=="__main__":
    atributos()