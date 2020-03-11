# /usr/bin/env python3
import numpy as np 
import matplotlib.pyplot as plt 

def grafica():
    sales=np.fromfile(r"D:\User\PythonProyectos\Numpy\salary.txt",dtype='float',sep=",")
    names= np.genfromtxt(r"D:\User\PythonProyectos\Numpy\employee.txt",dtype='str',delimiter=",")
    #obtener el numero segun el nombre para la comparacion
    new_names=names[2:-2]
    new_sales=sales[2:-2]
    x=np.arange(len(new_names))
    plt.xticks(x,new_names)
    plt.bar(x,new_sales)
    plt.title("Salarios vs Empleados")
    plt.xlabel("Empleados")
    plt.ylabel("Salario")
    plt.show()
    print("Report salario".center(50,"="))
    print("Max={}\nMin={}\nPromedio={}\nMediana={}\nSuma={}".format(np.max(new_sales),np.min(new_sales),np.average(new_sales),np.median(new_sales),np.sum(new_sales)))
    
if __name__=="__main__":
    try:
        grafica()
    except Exception as e:
        print(e)