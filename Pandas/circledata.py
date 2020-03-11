#usr/bin/env python
import pandas as pd 
import matplotlib.pyplot as plt 
ruta=r'Pandas\web_visitors.csv'
data= pd.read_csv(ruta,skiprows=0)
data.rename(columns={'fecha':'Fecha de visita'},inplace=True)
data.set_index('Fecha de visita',inplace=True)
colors=['yellowgreen','red','cyan','orange','green']
explot=(0.1,0,0,0,0)
data.plot(kind='pie',y='vistantes',shadow=True,explode=explot,legend=False,colors=colors)
plt.show()
