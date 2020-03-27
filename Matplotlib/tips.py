#/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def prueba():
    #plt.style.use('classic') #usaremos el estulo clasico de matplotlib.pyplot
    #fig=plt.figure()
    x=np.linspace(-10,10,1000)
    plt.plot(x,np.sqrt(np.abs(1-np.power(x,2))),'--r',label='Circle I')
    plt.plot(x,-np.sqrt(np.abs(1-np.power(x,2))),'-g',label='Circle II')

    plt.legend(loc='upper right')
    #fig.savefig('tip.png')
    plt.show()

def prueba2():
    x=np.linspace(-10,10,1000)
    plt.subplot(2,1,1) #filas, columnas y el numero del panel existente
    plt.plot(x,np.sqrt(np.abs(1-np.power(x,2))),'--r',label='Circle I')
    plt.legend(loc='upper right')
    plt.subplot(2,1,2) #segundo panel
    plt.plot(x,-np.sqrt(np.abs(1-np.power(x,2))),'-g',label='Circle II')
    plt.legend(loc='upper right')
    plt.xlabel('Valores de  X')
    plt.ylabel('Valores de Y')
    plt.show()
    
if __name__=="__main__":
    prueba2()