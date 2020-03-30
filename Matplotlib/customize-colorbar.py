#/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Graphic():
    #si queremos personalizar la barra de colores que se muestra podemos usar colorbar() y sus propiedades
    x=np.linspace(0,10,1000)
    I=np.sin(x)*np.cos(x[:,np.newaxis])
    #usamo imshow() cuando queremos mostrar grafico de matrices multiples
    plt.imshow(I,cmap='RdGy')
    plt.colorbar(label='Grafico virtual')
    plt.show()
    
def Graphic2():
    #elegir mapa  colores: Existen 3 categorias para elegir mapas de colores
    #mc: secuenciales, usando una continua secuencia de colores (binary,viridis)
    #mc: divergentes, usan  dos colores que muestran las desviacion positiva y negativa de una media
    #mc: cualitativos mezclan colores sin una secuencia en particular
    
    #fragmento de ejemplos
    plt.scatter([],[],c=['lista de colores'],s=['lista de tamaños'],cmap=plt.cm.get_cmap('viridis',5))

    #podemos usar la funcion plt.cm.get_cmap() para obtener cmap's
if __name__=="__main__":
    Graphic()