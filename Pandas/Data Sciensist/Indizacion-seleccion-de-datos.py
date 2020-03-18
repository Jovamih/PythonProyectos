#usr/bin/env python
import numpy as np
import pandas as pd
def indizacion():
    #usamos el operador IN para indicar si existe una clave (index)en la serie 
    data= pd.Series([12,34,45],index=['Hola','Adios','Visto'])
    print(data)
    val = 'Hola' in data
    #Usamos Keys(), index, items()
    print("Se encuentra el valor" if val else "No encontrado")
    print(data.keys())
    print(data.index)
    print(list(data.items()))
    for key ,values in data.items():
        print(key,values)
    #tambien se pueden hacer asignaciones de valor
    data['Hola']+=1
    print(data)
    #podemos hacer segmentaciones o Slicings
    #segementacion por indice explicito
    print(data['Hola':'Adios'])
    #egmentacion por indice entero implicito
    print(data[0:2])
    #Acceso por enmascaramiento(numpy)
    val=data[(data>30)]
    print(val)
    #indexacion elegante val=data[['Hola','Adios','Visto']]
    
def indizacion2():
    #tambie podemoss acccedder asus elementos con loc ,iloc e ix
    data=pd.Series([1,2,4,50],index=['Peru','China','Chile','Brazil'])
    #loc usa losmindices explicitos
    print(data.loc['Chile']) #error poner indices que no existen
    #iloc usa los indices implicitos 0,,1,..
    print(data.iloc[2:4])
if __name__=="__main__":
    indizacion2()