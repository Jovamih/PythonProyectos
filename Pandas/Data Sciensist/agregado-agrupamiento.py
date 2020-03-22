#/usr/bin/env python3
import numpy as np 
import pandas as pd 
from seaborn import load_dataset #paquete seaborn para obtener datos de prueba

class Data(object):
    
    def __init__(self):
        pass
    def getRelacion(self):
        alumno=list('ABCDDCBBAAAACDB')
        notas=np.random.randint(1,20,size=len(alumno))
        
        notas2=np.random.randint(1,20,size=len(alumno))
        data=pd.DataFrame({'Alumno':alumno,
                            'Notas':notas,
                            'Notas2':notas2})
        return data
    
    pass
        

def agregadoSimple():
    #pandas y numpy comparten algunas funciones devalor agregado
    #max,min,sum,meean,median,std(desviacion estandar),var(varianza)
    # Exclusivo de pandas: mad(desviacion media absoluta),count(),first(),last(),prod(producto de items)
    #cada uno soporta el parametro axis para indicar si es necesario las columnas que se operaran
    #OJO: Se aplican a los DataFrames y Series de pandas
    data=load_dataset('planets') #lista de planetas
    print(data.std())
    print(data.var())
    print(data.mad())
    print(data.count() ) # se aplica a filas de forma automatica data.count(axis=0)
   # print(data.first(1))
    #print(data.last(1)) solo soprta index de dataTimes
    #podemos usar pd.


def agrupamiento():
    #podemos usar groupby('columns') con otra funcion agregada para calcular lo que deseamos
   alumno=list('ABCDDCBBAAAACDB')
   notas=np.random.randint(1,20,size=len(alumno))
   data=pd.DataFrame({'Alumno':alumno,
                      'Notas':notas})
   print(data)
   print('agrupamiento por sum() y groupby()')
   data=data.groupby(data.Alumno).sum() #se pude incluir funciones devalors agreados al final
   print(data)
   #GruoupBy retorna un DataFrameGroupBy
   #podemos acceder acda columna de maner individual
   ser=data.groupby('Alumno')['Notas'].mean() # o mucho mejor podemos agregar <DataFrameGroupBy>.describe()
   print(ser)
   
def agrupamiento_aggregate():
    #otras formas de aplicar el agrupamiento es usando: aggregate()
   data=Data().getRelacion()
   df1=data.groupby(data.Alumno)['Notas'].describe()
   print(df1)
   #podemos demostrar ahora si aggregate()
   print('Funcion aggregate()')
   df2=data.groupby('Alumno').aggregate([np.min,np.max,np.mean]) #se puede especificar ['min',min,np.min] de todas esas maneras
   print(df2)
   #otra forma es passar un diccionario con los nombres de columna que se incluiran y su repectiva operacion
   df3=data.groupby('Alumno').aggregate({'Notas':np.min,'Notas2':'max'}) #o tambien se puede incluir como 'min'
   print(df3)
    
    
def agrupamiento_filter():
    #podemos tambien especificar un filtro que se aplique a  las columnas
    #la funcion 'filter' nos pemite soltar datos en funcion de las propiedades del grupo
    def func_filter(x):
        return x['Notas'].mean()>=10.5
    
    alumno=list('ABCDDCBBAAAACDB')
    notas=np.random.randint(1,20,size=len(alumno))
    
    notas2=np.random.randint(1,20,size=len(alumno))
    data=pd.DataFrame({'Alumno':alumno,
                        'Notas':notas,
                        'Notas2':notas2})
    print(data) # se interpreta como los alumnos que no tengan un promedio de notas mayor que 10.5 no se mostrarán
    df=data.groupby('Alumno').filter(func_filter)
    print(df)
    df=data.groupby('Alumno').filter(lambda x: x['Notas'].mean()>=10.5)
    print(df)
    
def agrupamiento_transformation():
    
    alumno=list('ABCDDCBBAAAACDB')
    notas=np.random.randint(1,20,size=len(alumno))
    
    notas2=np.random.randint(1,20,size=len(alumno))
    data=pd.DataFrame({'Alumno':alumno,
                        'Notas':notas,
                        'Notas2':notas2})

    df=data.groupby('Alumno').transform(lambda x:x-x.mean())
    print(df)
    
def metodos():
    #podemos usar apply() puesto que es bastante fleexible toma como parametro un DataFrame
    #y retorna un objeto pandas o escalar
    data=Data().getRelacion()  
    def apply_func(x):
        x['Notas']+=1
        return x
    
    df=data.groupby('Alumno').apply(apply_func)
    print(df)
    #podemos proporcionar metodos de agrupacion
    #mapeo
    df=data.set_index('Alumno')
    mapping={'A':'Destacado','B':'Regular','C':'Ineficiente'}
    df=df.groupby(mapping).max()
    print(df)
    #tambien podemos acceder atraves de los indices [str.lower,mapping]
    
    
if __name__=="__main__":
    metodos()