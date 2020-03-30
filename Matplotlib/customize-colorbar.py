#/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Graphic():
    #si queremos personalizar la barra de colores que se muestra podemos usar colorbar() y sus propiedades
    x=np.linspace(1,10,1000)
    I=np.sin(x)*np.cos(x[:,np.newaxis])
    #usamo imshow() cuando queremos mostrar grafico de matrices multiples
    plt.imshow(I)
    plt.colorbar(label='Grafico virtual')

    plt.show()

if __name__=="__main__":
    Graphic()