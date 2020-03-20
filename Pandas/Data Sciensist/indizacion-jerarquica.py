# /usr/bin/env python3

import pandas as pd 
import numpy as np

def indizacion():
    #Podemos creer indices multiples atravez de lista de tuplas
    index=[('Peru',2010),('Chile',2006),('China',2000),('Peru',2020),('China',2001)]
    population=[86623,34753,34765,50954,54774.3]
    index=pd.MultiIndex.from_tuples(index)
    
    data=pd.Series(population,index=index)
    print(data)
    #podemos reasignar indices con data.reindex(indice)
    #Accedemos a  loss datos de cada indice : data.loc['Peru',:]
    #podemos convertir un indice multiple de una 'Series' en un DataFrame convensional
    #metodo unstack()
    data_df=data.unstack()
    print(data_df.fillna(axis=1,method='ffill').fillna(0))
 
 #constructores explicitos de multiples indices
def indizacion1():
     index=[['a','a','b','b','c','c','d','d'],[1,2,1,2,1,2,1,2]]
     index_1=pd.MultiIndex.from_arrays(index)
     print(index_1)
     
     index=[('Peru',2010),('Chile',1990),('Peru',2020)]
     index_2=pd.MultiIndex.from_tuples(index)
     print(index_2)
     
     index=[[2000,2002,2004,2020],['Natalidad','Mortalidad']]
     index_3=pd.MultiIndex.from_product(index,names=['años','Estadistica'])
     #se puden asgnar los nombres como series.index.names=['something','something']

def indizacion2():
    periodo=['I','II']
    pais=['Peru','Chile','China','Argentina','Brasil']
    anio=[2000,2002,2010,2018,2020]
    estadistica=['Natalidad','Mortalidad']
    population=[86623,34753,34765,50954,54774.3]
    #para facilitarnos el acceso  a las matrices incorpordas en panda contamos con la funcion
    #nativa de Python slice(), pero pandas nos facilita la vida con pd.IndexSlice
    index=pd.MultiIndex.from_product([pais,periodo],names=['Pais','Periodo'])
    columns=pd.MultiIndex.from_product([anio,estadistica],names=['Año','Estadisticas'])
    dat=np.random.randint(3000000,9999999,size=(10,10))
    data=pd.DataFrame(dat,index=index,columns=columns)
    print(data)
    print("Valores con indizacion IndexSlice()->Mortalidad en cada pais durante el primer periodo")
    idx=pd.IndexSlice
    
    print(data.loc[idx[:,'I'],idx[2002:,'Mortalidad']])
    #podemos acceder atraves de indexadores loc,iloc[row,column]
    print(data.loc[:,2002]) #podemos ser mas especificos data.loc[:,(2002,'Natalidad')]
    
def ordenamiento_indices():
    #La mayoria de operaciones MultiIndex falla cuandos los idx estan desordenados
    ser=pd.Series([12,34,44.2,34],index=list('adcb'))
    print(ser)
    #metodo sort_index(inplace=True) sin parametros, en base a el indice -->inplace=True
    ser.sort_index(inplace=True)
    #metodo sort_values(by=[columnas_name],inplace=True) mediante una columna  --> inplace=True
    print(ser)
    #asignamiento de indices: reset_index(name='columna') o set_index('columna',inplcae=True)
    frame=pd.DataFrame(np.random.randint(1,80,size=(3,4)),index=list('abd'),columns=list('1234'))
    #print(frame)
    #frame.reset_index(drop=True,inplace=True)
    #print(frame)
    frame.set_index('1',inplace=True) #si son indices multiples set_index(['name1','name2'],inplace=True)
    print(frame)
    
def datos_agregados():
    periodo=['I','II']
    pais=['Peru','Chile','China','Argentina','Brasil']
    anio=[2000,2002,2010,2018,2020]
    estadistica=['Natalidad','Mortalidad']
    #para facilitarnos el acceso  a las matrices incorpordas en panda contamos con la funcion
    #nativa de Python slice(), pero pandas nos facilita la vida con pd.IndexSlice
    index=pd.MultiIndex.from_product([pais,periodo],names=['Pais','Periodo'])
    columns=pd.MultiIndex.from_product([anio,estadistica],names=['Año','Estadisticas'])
    population=np.random.randint(3000000,9999999,size=(10,10))
    data=pd.DataFrame(population,index=index,columns=columns)
    print(data)
    #DataFrame incluye funciones de valor agregado mean() sum() min()
    print("Valores agregados")
    #frame=data.sum(level='Pais')
    frame= data.mean(level='Año',axis=1) #podemos acceder a las subcolumnas especificando la funcionalidad con 'axis'
    print(frame)
    
    
if __name__=="__main__":
    datos_agregados()