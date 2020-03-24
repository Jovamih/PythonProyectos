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
    print(ser['2000-10-12':'2000-10-24'])
    #podemos filtra los elemntos por año
    print(ser['2000'])
#estructuras de datos de series temporales de pandas
#para las marcas de tiempo pandas proporciona..> TimeStamp() con estructura de indice asociadda DatatimeIndex()

#para periodos de tiempo tenemos a Period() con estructura de indice PeriodIndex()
#para deltas de tiempo o duraciones tenemos a TimeDelta() con index TimedeltaIndex()

if __name__=="__main__":
    series()