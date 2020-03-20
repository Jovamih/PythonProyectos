# !usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
ruta=r'D:\User\PythonProyectos\Pandas\hubble_recesion.csv'
#data=pd.read_csv(ruta)d
data= pd.read_csv(ruta,sep=',')
data.set_index('distancia',inplace=True)
data.sort_values(by=['distancia'],inplace=True)
data.plot()
plt.legend(loc='upper center')
plt.show()
print(type(data))
