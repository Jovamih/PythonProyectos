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
    
def dataframes():
    #acceso modo diccionario
    population_dict={'China':120000000,
                'Peru':90000,
                'Chile':89098830,
                'Colombia':120000,
                'Argentina':1299000
                }
    infected_dict={
                'China':890000,
                'Peru':900,
                'Chile':89000,
                'Colombia':52009,
                'Argentina':1230
            }
    population=pd.Series(population_dict)
    infected=pd.Series(infected_dict)
    data=pd.DataFrame({'Poblacion':population,'Infectados':infected})
    print(data)
    print(data['Poblacion'])
    print(data.Poblacion) #se dee evitar usar este tipo de acceso por seguridad
    #tambien se pueen crear otras columnas
    data['Porcentaje']=(data['Infectados']/data['Poblacion'])*100
    print(data)
    #Transposicion de columnas
    print(data.T)
    
def dataframe_index():
    #accesos a los datframes
    #acceso por enmascaramiento
    population_dict={'China':120000000,
                'Peru':90000,
                'Chile':89098830,
                'Colombia':120000,
                'Argentina':1299000
                }
    infected_dict={
                'China':890000,
                'Peru':900,
                'Chile':89000,
                'Colombia':52009,
                'Argentina':1230
            }
    population=pd.Series(population_dict)
    infected=pd.Series(infected_dict)
    data=pd.DataFrame({'Poblacion':population,'Infectados':infected})
    data['Porcentaje']=(data['Infectados']/data['Poblacion'])*100
    #tenemos indeacion implicita a traves de indice snetros e explicita (nombre verdaderos)
    print(data.iloc[4,:])
    #explicita
    print(data.loc['Chile':'Argentina',:])
    print(data.loc[data['Porcentaje']>30]) # se puede poner sin loc, si solo se hace referencia a la fila data[data.something>do]
    print(data.loc[data.Porcentaje>10,['Poblacion']])
    #posee propiedaes similares a las matricez Numpy
    #slicing
    print(data.loc[:,'Poblacion':'Infectados'])
    print(data['Colombia':'Argentina']) #solo podemos acceder a las filas
    #con data['Colombia']: accedemos a las columnas
    #Lod tipos de acceso por enmascaramiento y por indexacion eleante se pueden  combinar
    
if __name__=="__main__":
    dataframe_index()