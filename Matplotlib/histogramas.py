#/usr/bin/env python
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
#los histogramas sirven para representar variables cuantitativas en Graficas
#como distribucion de personas por el rango de edad presentado .etc
def histogramas():
    #la mayoria de histogramas se representan de forma simple
    data=np.random.randint(1,100,size=100)
    plt.hist(data,bins=6,color='green',histtype='bar',alpha=0.5)
    #plt.hist()
    plt.show()
    #si lo que queremos en contar el numero de ocurrencias dentro de cada contenedor(bin) dado
    #sin mostrar el grafico podems recurrir a la funcion  de Numpy histogram
    #np.histogram(data,bins=10) : data->los datos, bins->Los contenedores o intervalos de datos parejos
    counts,bin_edges=np.histogram(data,bins=6)
    for (count,_bin) in zip(counts,bin_edges):
        print("{} -> {} ocurrencias".format(_bin,count))
        
    #podemos tamien reutilizar fragmentos de codigo para vada grafica hist() que necesitamos analizar
    data1=np.random.normal(-10,10,100)
    data2=np.random.normal(-10,10,100)
    data3=np.random.normal(-10,10,100)
    #normed ya quedo en desiuso y se recomienda usar density
    kwargs=dict(histtype='stepfilled',alpha=0.3,density=True,bins=20)
    plt.hist(data1,**kwargs)
    plt.hist(data2,**kwargs)
    plt.hist(data3,**kwargs)
    plt.show()
    
def histograma2d():
    #podemos tener histogramas en dos dimensiones
    #para ello utilizaremos una distribucion normal multivariada
    mean=[0,0]
    cov=[[1,1],[1,2]]
    x,y=np.random.multivariate_normal(mean,cov,100000).T
    plt.hist2d(x,y,bins=20,cmap='Blues')
    cb=plt.colorbar()
    cb.set_label('Cantidad por contenedores')
    plt.show()
    
def histogramaHex():
    mean=[0,0]
    cov=[[1,1],[1,2]]
    x,y=np.random.multivariate_normal(mean,cov,100000).T
    plt.hexbin(x, y, gridsize=30, cmap='Blues')
    cb = plt.colorbar(label='count in bin')
    plt.show()

if __name__=="__main__":
    histogramaHex()