#/usr/bin7env python3
import numpy as np 
import pandas as pd

def missing():
    #manejo de dato faltante en python. con pandas
    #incorpora el modelo centinela mediante los objetos None(Nativo) y NaN
    #None: objeto nativo en python que representa la ausencia de datos en el codigo
    a=pd.Series([n**2 for n in range(12)])
    print(a)
    #a.append(np.nan)
    #aplicar una funcion agregada sobre una matriz si este posse un None genera error
    #NaN: Not A Number  -> Ausencia de valores en matrices Numpy
    #OPERANDO CON VALORES NULOS
    #isnull(): Detecta valores nulos -->Devuelve una mascar Boleana
    #notnull():Detecta valors no nulos (valores normales) -->Return Mascara Booleana
    #dropna(): Devuelve una lista filtrado con los objetos no nulos
    #fillna(): devuelve unna copia de datos con los valores faltantes rellenados
    #Las MASCARAS booleanas se puden usar como un indice Series o DataFrame
    m=a.isnull()
    print("Valores nulos: {}".format(a[m]))
    m=a.notnull()
    print("Valores no Nulos: {}".format(a[m]))
    data=pd.DataFrame([[12,34,2],[None,None,None],[90,23,21],[10,None,10]])
    print('Datos completos')
    print(data)
    print('Datos filtrados')
    print(data.dropna(axis='rows'))
    #print(data.dropna())
    print('Datos filtrados por columa how=all')
    print(data.dropna(axis='columns',how='all'))
    print('Datos filtrados por columna para un minimo de elementos no Nulos')
    print(data.dropna(axis='columns',thresh=3))
    
def missing1():
    data=pd.DataFrame([[12,34,2],[None,None,None],[90,23,21],[10,None,10]])
    print(data)
    #print(data.fillna(0))
    
    #tambien poseemos metodos de relleno. 
    #method='ffill' hacia adelante
    #method='bfill' hacia atras
    print(data.fillna(axis="rows",method='ffill'))
    data[data.isnull()]=0
    #print(data)
        
if __name__=="__main__":
    missing1()