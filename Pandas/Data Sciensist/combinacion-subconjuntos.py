# /usr/bin/env python3
import pandas as pd 
import numpy as np

def make_df(cols='ABCD',ind=range(2)):
    info={ c: [str(c)+ str(i) for i in ind]
        for c in cols
    }
    return pd.DataFrame(info,index=ind)

def make_fr(cols=list('ABCD'),ind=range(2)):
    info=[[str(i)+str(e) for i in cols] for e in ind]
    return pd.DataFrame(info,index=ind,columns=cols)

def combinacion_DataSets():
    #combinacion de conjunto de datos DataSets con Concatenate() y concat()
    a=np.random.randint(1,200,size=(5,8))
    b=np.random.randint(34,890,size=(5,10))
    
    c=np.concatenate([a,b],axis=1)
    print(c)

    print('Concatenando Series de Pandas')
    #combinacion de Datasets con concat del paquete Pandas--> pd.concat
    #se aplica para series y DataFrames
    ser1= pd.Series(np.random.randint(1,200,size=3),name='Indice')
    ser2=pd.Series(np.random.randint(1,200,size=4),index=range(3,7),name='Indice')
    
    c=pd.concat([ser1,ser2],axis=0)
    print(c)
    p1= make_fr(list('ABCD'),range(3))
    p2=make_fr(list('CDEF'),range(3))
    
    c1=pd.concat([p1,p2],axis=0,ignore_index=True).fillna(axis=0,method='ffill') #tambien se pudo usar axis='columns'
    print(c1)
    #recomendacion: ignore_index=True--> cuando el indice no importa se recmienda ignorarlo para una concatenacion limpia
    #añadiendo etiquetas a las fuentes de datos con key
    c1=pd.concat([p1,p2],axis=0,keys=['Datos 1','Datos 2'])
    print(c1)
    #concat tambien nos permite especificar el tipo de uniion de datos 
    print("Fusion de datoss con join='inner'")
    #el tipo por defecto pd.concat(join='outer'), asi que podemos extennder a join='inner' para que intesecte las columnas
    c1=pd.concat([p1,p2],axis=0,keys=['D1','D2'],join='inner')
    print(c1)
    print("Podemos lograr un efecto similar a pd.concat() con append()")
    c1=p1.append(p2)
    print(c1)
    
    
if __name__=="__main__":
    combinacion_DataSets()