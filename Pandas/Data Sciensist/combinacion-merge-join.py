# /usr/bin/env python3

import pandas as pd 
import numpy as np

#existen categorias de combinaciones
#basadas en Merge: uno a uno,muchos a uno, muchos a muchos
class Data(object):
    
    def __init__(self):
        pass
    def getUsuario(self):
        return pd.DataFrame({
        'Usuario':['Johan','Amparo','Angie','Steven'],
        'Edad':[18,18,20,21],
        'idPais':[1,2,2,4],
        'idMatricula':[1,2,4,4],
        'dato':list('ABCE')
    })
        
    def getPaises(self):
        return pd.DataFrame({
        'idPais':[1,2,3,4,5],
        'NombrePais':['Peru','España','Colombia','Australia','Oceania']
    })
        
    def getPaisN(self):
        return pd.DataFrame({
        'id':[1,2,3,4,5],
        'Nombre':['Peru','España','Colombia','Australia','Oceania'],
        'dato':list('PECAO')
    })
        
    def getMatriculas(self):
        return pd.DataFrame({
        'idMatricula':[1,1,2,3,4,4,3],
        'curso':['Matematicas','Lenguaje','Base de Datos','Contabilidad','Unity','Adobe8','UdemyPRO']
    })    
     
    pass   

def make_df(cols=list(),idx=tuple()):
    info={ e: [ str(e)+str(i) for i in idx]
         for e in cols
    }
    return pd.DataFrame(info,index=idx)


def combinacion():
    #tipo de expresion de conbinacion simple: uno a uno 
    data1=make_df(['Usuario','Password'],range(6))
    data2=make_df(['Usuario','Last Activity'],range(6))
    
    print('Fusion de datos con merge')
    dtmerge=pd.merge(data1,data2)
    print(dtmerge)
    print('Combinacion muchos a uno')
    #categoria Muchos a uno
    data1=Data().getUsuario()
    
    data2=Data().getPaises()
    data3=Data().getMatriculas()
    dtmerge=pd.merge(data1,data2)
    print(dtmerge)
    print('Combinacion de muchos a muchos')
    dtmerge=pd.merge(data1,data3)
    print(dtmerge)
    
#aveces el nombre de la columna no coincidira con la otro fuente de datos por lo que
#se tendra que especificar una clave de combinacion

def clavesCombinacion():
    #para poder especificar que columnas tenemos que fusion de forma exolicita usamos :ON
    #para facilitar la legibilidad
    data1=Data().getUsuario()
    data2=Data().getPaises()
    rs=pd.merge(data1,data2,on='idPais')
    print(rs)
    #para especificar las columnas de las fuentes de datos si estas no coinciden usamos
    #left_on y right_on
    data2=Data().getPaisN()
    rs=pd.merge(data1,data2,left_on='idPais',right_on='id').drop('id',axis='columns')
    print(rs)
    #especificar la union atraves de indices podemos usar left_index y right_index=True
    #rs=pd.merge(data1,data2,left_index=True, right_index=True) como tambien podemos alternarlos segun
    #sea nuestra necesidad (mezclar un indice con una coolumna en comun etc.)
    
def set_arithmethics():
    #podemos especificar la forma en la que los datos se uniran
    #usando inner,outer,left,right
    data1=Data().getUsuario()
    data2=Data().getMatriculas()
    
    rs=pd.merge(data1,data2,on='idMatricula',how='outer').dropna(axis='rows',how='any')
    print(rs)

    #Nombres de columnas superpuestas: puede darse el caso en el que las columnas entren en 
    # y necesitamos agregar un sufijo para que la fusion sea apropiada sufixes=['_R','_L']
    data1=Data().getUsuario()
    data2=Data().getPaisN()
    try:
        rs=pd.merge(data1,data2,left_on='idPais',right_on='id',suffixes=('_user','_mat')).drop('id',axis='columns')
        print(rs)
    except Exception as e:
        print(e)
        
        
        
        
if __name__=="__main__":
    set_arithmethics()