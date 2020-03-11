# /usr/bin/env python3
import numpy as np 

def operadores():
     a=np.random.randint(3,10,size=10)
     b=np.random.randint(4,78,size=10)
     print(np.add(a,b))
     print(np.subtract(b,a))
     print(np.negative(a,b))
     print(np.multiply(a,b))
     print(np.divide(a,b))
     print(np.floor_divide(b,a))
     print(np.power(b,a))
     print(np.mod(b,a))
     #funion abs
     #abs() : integrada en python
     #np.abs() o np.absolute() : integrada en numpy
     

if __name__=="__main__":
    operadores()