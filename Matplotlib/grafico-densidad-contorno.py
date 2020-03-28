#/usr/bin/env python3
import matplotlib.pyplot as plt 
import numpy as np 


#a veces es util mostrar datos tridimensionales en dos dimensiones
#utilizando contornos o regiones codificadas por colores
#las funciones aptas para ello son:     plt.contour(), plt.countf(),plt.imshow(_mostrar imagenes_)
def f(x,y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

def grafico():
    #usaremos la funcion plt.countour() para graficar dichos datos, esta toma 3 paraemtros x,y,z
    x=np.linspace(-10,10,1000)
    y=np.linspace(-10,10,100)
    #antes de pasarlas como parametro debemos preprarlas con np.meshgrid() que contruye
    #cuadriculas biddmiensionales a traves de maatrices unidimensionales
    X,Y=np.meshgrid(x,y)
    Z=f(X,Y)

    plt.contourf(X,Y,Z,cmap='RdGy') #RdGy = RedGray # se aplica al relleno de curvas
    #podemos usar plt.contour(X,Y,Z,colors='something') solo para lineas de trzado
    plt.colorbar() # colorbar se desenvuelve mejor con contourf() de reelleno
    plt.show()
    
    
    
#otros usos para imshow()
#contours = plt.contour(X, Y, Z, 3, colors='black')
#plt.clabel(contours, inline=True, fontsize=8)
#plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower',
#          cmap='RdGy', alpha=0.5)
#plt.colorbar();


if __name__=="__main__":
    grafico()