#/usr/bin/env python

import pandas as pd
import numpy as np
import numexpr
def rendimiento():
    #la libreria numexpr proporciona eval() funcion que evalua literales de cadena a expresiones python logicas
    data=pd.DataFrame(np.random.randint(12,200,size=(8,4)),columns=list('ABCD'))
    #la libreria Pandas tambien posee pd.eval() para operar atraves de estos
    data_mask=pd.eval('data.A>100')
    print(data[data_mask])
    #podemos usar eval() en python en asignaciones internas 
    data.eval('TOTAL=A+B+C+D',inplace=True)
    print(data)
    #el uso particular de eval() es para sumas y gestion de columnas de forma mas rapida y eficiente
    #tambien podemos usar query() y combinarlos con el uso de variables temporales
    data_mean=(data.mean(axis=0)).mean()
    data_mask=data.query('(A>@data_mean )& (D>@data_mean)')
    print(data[data_mask])
    
    
    
if __name__=="__main__":
    rendimiento()