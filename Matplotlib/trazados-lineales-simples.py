#/usr/bin/env python3

import numpy as np 
import matplotlib.pyplot as plt 

def trazado():
    fig=plt.figure()
    axes=plt.axes()

    x=np.linspace(-10,10,1000)
    axes.plot(x,np.sin(x))
    #plt.show()
    #podemos aplicar colores a las tramas
    
    for i in range(10):
        plt.plot(x,np.sin(x-i))
    plt.show()
def trazado1():
    x=np.linspace(-10,10,1000)
    plt.plot(x,np.cos(x-1),color='blue') #podemos indicar codigos hexadecimales, abreviados, colores RGB () u otros
    plt.plot(x,np.sin(x-3),'--r') #podemos ndicar la forma de la curva y el color (shape/color)
    plt.show()
    
def trazado2():
    x=np.linspace(-10,10,1000)
    #podemos definir el estilo de trazado
    plt.plot(x,x-1,color='green',linestyle='solid')
    #los estilos se puden especificar como
    #linestyle='solid' o '-'
    #   'dashed' o '--'
    #   'dashdot' o '-.'
    #   'dotted' o ':'
    plt.plot(x,x+12,color='red',linestyle=':')
    #ambien podemos especificar el color y el estilo pero esta vez sin parametroa adicionales
    plt.show()
    #':r' ->dotted color rojo

    #'--b' -->dashed color azul
    
def trazado3():
    #podemos establecer los limites de las grafica con xlim() y ylim()
    plt.style.use('seaborn-whitegrid')
    x=np.linspace(-10,10,1000)
    plt.plot(x,np.log(np.abs(x)),'-g',label='Funcion  Y=X-1')
    #plt.xlim(-20,20)
    #plt.ylim(-10,10)
    plt.axis('equal') #para ajustar de forma equitativa los ejes
    plt.xlabel('Eje X')
    plt.ylabel('Eje X')
    plt.title('Grafico funcional de prueba')
    plt.legend()
    
    #tambien podemos ajustar los limites a las coordenadas actuales con axis(tight)
    #podemos graficar
    plt.show()

if __name__=="__main__":
    trazado3()