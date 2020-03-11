# usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt 
def read(csv):
    #cells=['ID','Nombre','Apellido','Nacimiento','Domicilio','Email','Observacion','DNI']
    data=pd.read_csv(csv)
    data.head()
    print(data)
    print(data["nombre"])
if __name__=="__main__":
    read(r"D:\User\PythonProyectos\Pandas\Pacientes.csv")
    