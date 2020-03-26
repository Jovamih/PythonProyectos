#/usr/bin/env python3

import numpy as np 
import pandas  as pd

def series():
    #podemos hacer arrays numpy de tiempo np.array('2019-10-12',dtype=np.datetime64)
    #para ello contamos con el paquete pandas de python
    
    index=pd.DatetimeIndex(['2000-10-12','2000-10-24','2001-12-12'])
    ser=pd.Series([12,54,67],index=index)
    print(ser)
    #podemos acceder a cada elemnto como un pandas normal
    print(ser['2000-10-01':'2000-10-24'])
    #podemos filtra los elemntos por año
    print(ser['2000'])
#estructuras de datos de series temporales de pandas
#para las marcas de tiempo pandas proporciona..> TimeStamp() con estructura de indice asociadda DatatimeIndex()

#para periodos de tiempo tenemos a Period() con estructura de indice PeriodIndex()
#para deltas de tiempo o duraciones tenemos a TimeDelta() con index TimedeltaIndex(
    
def series1():
    #podemos crear periodos de fechas simultaneamente
    #podemos reeplmzara formas anteriores y comprarlas con esecto a la creacion d indices
    index=pd.DatetimeIndex(['20000-12-12','2003-12-23'])
    #es equivalente a
    index=pd.to_datetime(['2000-12-23','2003-12-23']) #pero este posee mas caracteristicas
    
    index=pd.date_range(start='2000-12-23',end='2003-12-12',periods=90) #o se puede usar frecuencias con 'freq'
    index=pd.date_range(start='2020-3-24',periods=9,freq='D')#o podemos usar freq='5D3H2T': 5 dias 3 horas y 2 minutos
    
    index=pd.preiod_range(start='2000',period=12,freq='M')
    #usaremos eval() cuando queramos gacer operaciones con columnas
    #data['coluns']=data.eval('columns1+column2')

if __name__=="__main__":
    series()