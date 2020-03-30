#/usr/bin/env python3

import numpy  as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcess

plt.style.use('seaborn-whitegrid')
def visualizacion():
    #podemos visualizar errores mas ciomunes usandio funciones plot incluidas en mmtplotlib.pyplot
    dy=0.89
    x=np.linspace(-10,10,1000)
    y=np.sin(x)+dy
    
    plt.errorbar(x,y,yerr=dy,fmt='--',color='black',ecolor='lightgray',elinewidth=2,capsize=0)
    plt.axis('tight')
    #plt.legend()
    plt.show()

def errores_continuos():
    #errores conitnuos
    pass

if __name__=="__main__":
    visualizacion()