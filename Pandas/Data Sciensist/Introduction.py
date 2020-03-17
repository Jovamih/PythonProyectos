# /usr/bin/env python3
#en Pandas existen 3 tios fundamentales de datos estructurados
#las Series, DataFrames, Index

import pandas as pd
import numpy as np

def series():
    data=pd.Series([12,34,56,7.8])
    print(data)
    data=pd.Series([12,34,565.33,23,44,122], index=["Notas","Edad","Grande","code","Gemelas","122N"])
    print(data)
    print(data.values)
    print(data.index)
    
    #se puede construir un objeto Series de un objeto Dict en python
def series_dict():
    population_dict={'China':123000000.2,
                     'Colombia':2340000,
                     'Peru':24240000,
                     'Chile':769000000,
                     'Rusia':120000000
                     }
    data=pd.Series(population_dict)
    print(data)
    print(data['China'])
    data['China']+=1
    print(data['China'])
    #un Series acepta como parametro principal un objeto 'data' que puede ser un diccionario
    #lista,tupla array Numpy
    #Se pueden especificar indices explicitos para cada tipo de dato pd.Series(data,index=[something,something])
    
def dataframes():
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
    datos={'Habitantes':population_dict,
           'Infectados':infected_dict
        }
    data=pd.DataFrame(datos)
    print(data)


if __name__=="__main__":
    #series()
    #series_dict()
    dataframes()