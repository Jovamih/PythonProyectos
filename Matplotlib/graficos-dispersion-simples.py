#/usr/bin/env python3
import matplotlib.pyplot as plt 
import numpy as np

def dispersion():
    x=np.linspace(-20,20,100)
    y=np.sin(x)
    
    plt.plot(x,y,'-^',color='black') #podemos especificar '-ok'
    #la estrcutura del 3er argumento de la declaracion de plot() es 'linea de separacion|disperso|color'
    #los marcadores de dispersion puden ser: [o,>,<,^]
    #plt.show()
    #pero la mejor herramienta para hacer dispersiones es plt.scatter()
    plt.scatter(x,y,marker='o')
    plt.show()
    
    

def dispersionAdvanced():
    #la diferencia de usar plt.scatter y no plt.plt es que la primera nos permiye asignar
    #propiedades indivuales a cada punto (color tamaño transaparencia)
    
    #obtendremos rangso de valors aleatorios para demstrarlo
    rng=np.random.RandomState(0)
    x=np.random.randint(10,200,size=100)
    y=np.random.randint(20,200,size=100)
    color=rng.rand(100)
    size=100*rng.rand(100)
    
    plt.scatter(x,y,c='green',s=size,alpha=0.5,cmap='viridis')
    plt.axis('tight')
    plt.colorbar()
    plt.show()
    
if __name__=="__main__":
    dispersionAdvanced()