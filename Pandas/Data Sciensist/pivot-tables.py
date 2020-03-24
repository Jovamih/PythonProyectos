#/usr/bin/env python3
import numpy as np
import pandas as pd
from seaborn import load_dataset
import matplotlib.pyplot as plt

def pivot():
    #podemo usar pivot para mostrar una mejor vista
    #pibot usala funcion de agregado  mean() por defecto en aggfunc='mean'
    data=load_dataset('titanic')
    a=data.pivot_table('survived',index='sex',columns='class')
    print(a)
    #ppodemos usar pd.cut() apara greagr mas indices
    ages=pd.cut(data['age'],[0,18,80])
    a=data.pivot_table('survived',index=['sex',ages],columns='class')
    print(a)
    #pivot tambien posee fill_value para asignar valores por defcto
    #dropna: para borrar columnas  que no poseen datos True por defecto
    #podemos graficar datos con matplotlib
    
def datosAdvanced():
    data=pd.read_csv('births.csv',sep=',')
    a=data.pivot_table('births',index='year',columns='gender',aggfunc='sum')
    a.plot()
    plt.ylabel('Total de nacimientos por decada')
    plt.show()
    
def explorarcion_datos():
    pass
    #pronta implementacion
    
if __name__=="__main__":
    datosAdvanced()