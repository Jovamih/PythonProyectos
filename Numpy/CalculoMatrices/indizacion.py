# /usr/bin/env python3
import numpy as np 
def indice():
    print("Indices de lujo")
    #indizacion de lujo nos permite acceder a mas de un elemento en una sola indizacion
    #a[0]: indizacion simple (en este ej. accedemos al primer elemento)
    # index=[0,3,2,1,0,0]; 
    # a[index]: aqui accedemos a multiples elementos
    index=[0,2,3,2,1,0,0,1]
    a=np.random.randint(9,12,size=30)
    print(a[index])
    a=np.random.randint(9,12,size=(5,5))
    indX=[0,0,1,2,3,1]
    indY=[1,2,2,1,1,1]
    print(a[indY,indX])
    
def indicesCombinados():
    print("Indices combinados")
    #indices elegantes y simples
    a=np.random.randint(9,12,size=(8,4))
    print(a)
    print("Indices elegantes y simples")
    a0=a[2,[0,2,1,0]]
    print(a0)
    print("Indices elegantes y de corte")
    print(a[::3,[0,3,3,2]])
    print("Indices elegantes y de")
    a[::3,[0,2,2,1]]=99
    print(a)
    
def indicesAsignacion():
    
    pass
    
if __name__=="__main__":
    indice()
    indicesCombinados()