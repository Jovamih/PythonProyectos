#usr/bin/env python3
import pandas as pd 
import matplotlib.pyplot as plt
ruta1=r'Pandas\web_visitors.csv'
ruta2=r'Pandas\web_newvisitors.csv'
data0=  pd.read_csv(ruta1,skiprows=0)
data1= pd.read_csv(ruta2,skiprows=0)
data_merge= pd.merge(data0,data1)
data_merge.rename(columns={"fecha":"Fecha de Visita"},inplace=True)
data_merge.set_index('Fecha de Visita',inplace=True)
data_merge.sort_values('Fecha de Visita',inplace=True,ascending=True)

print(data_merge.head())
data_merge.plot()
plt.show()
