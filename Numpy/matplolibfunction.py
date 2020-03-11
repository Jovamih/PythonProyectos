# /usr/bin/env python3
import numpy as np 
import matplotlib.pyplot as plt

x=np.linspace(1,10,100)
y1=np.cos(x)
y2=np.sin(x)
plt.plot(x,y1,'-r',label="coseno")
plt.plot(x,y2,'-g',label="seno")
plt.legend(loc="center")
plt.xlabel("X extension")
plt.ylabel("Y extension")
plt.ylim(-2.5,2.5)
plt.xlim(0,10)
plt.show()