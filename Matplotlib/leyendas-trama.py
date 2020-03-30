#/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Graphic():
    #podemos especificar mas personalizacion a las leyendas de graficos
    x=np.linspace(-20,20,1000)
    y1=np.sin(x)
    y2=np.cos(x)
    plt.plot(x,y1,'-g',label='Funcion Seno Y=sen(X)')
    plt.plot(x,y2,'--r',label='Funcion Coseno Y=cos(X)')
    plt.legend(loc='upper right',frameon=False,ncol=2)
    #podemos usar FrameOn para deactivar el marco de la leyenda
    #ncol: para especificar el numero de columnas en la leyenda
    
    plt.axis('equal')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.show()


def Garphic2():
    pass

if __name__=="__main__":
    Graphic()