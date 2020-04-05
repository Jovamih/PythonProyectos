# /usr/bin/env python3

import numpy as np 
import pandas as pd

def operaciones():
    #debido a quee pandas necesita de Numpys este puede usar los uFuncs de Numpy
    #np.sin,cos,tans,arctan.arcsin,exp
    ser= pd.Series(np.random.randint(1,90,size=8))
    df= pd.DataFrame(np.random.randint(1,90,size=(4,5)),index=['a','b','c','d'],columns=['P1','P2','P3','P4','P5'])
    print(ser)
    print(df)
    print("With uFuncs")
    print(np.sin(ser))
    print(np.exp2(df))
  
#alineacion de indices  en Series
def op_series():
    dat1=pd.Series([1,2,4,46,6,464,335,33],index=list('abcdefgh'))
    dat2=pd.Series([1,2,45,54,24],index=list('abdth'))
    A=dat1+dat2
    print(A)
    A=dat1.add(dat2,fill_value=0)
    print(A)
#alineacion de indices en dataframes
#podemos hacer operaciones Pandas con funciones personalizadas de estos mismos
# (+) : add()
# (-) : sub() o substract()
# (*) : mul() o multiply()
# (/) : div(), divide() o truediv()
# (//): Division entera-> floordivide()
# (%) : mod()
#(**) : pow()
#pandas permite usar estas funciones atraves de los objetos mismos a diferencia de Numpy
# Por ejemplo
# para multiplicar (*) : en Numpy np.mupltiply(A,B), pero en pandas A.multiply(B)

#con la facilidad de poder agregar valores de relleno en caso no se puedan alinear los indices en la operacion
#esto gracias al paramatro fill_value que se encuentra embebido en cada funcion de operador de pandas
#A.sub(B,fill_value=0) ojo: funciona entrea operaciones de 2 dataframes


def op_dataframe():
    df2= pd.DataFrame(np.random.randint(1,90,size=(4,5)),index=['a','b','c','d'],columns=['P1','P2','P3','P4','P5'])
    df1= pd.DataFrame(np.random.randint(1,90,size=(4,5)),index=['a','b','c','d'],columns=['P1','P2','P3','P4','P5'])

    A=df1+df2
    B=df1-df2.iloc[0]
    #B=df1.sub(df2,axis=0)
    print(A)
    print(B)


if __name__=="__main__":
    #operaciones()
    op_dataframe()