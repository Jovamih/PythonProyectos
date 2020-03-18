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
def op_dataframe():
    df2= pd.DataFrame(np.random.randint(1,90,size=(4,5)),index=['a','b','c','d'],columns=['P1','P2','P3','P4','P5'])
    df1= pd.DataFrame(np.random.randint(1,90,size=(4,5)),index=['a','b','c','d'],columns=['P1','P2','P3','P4','P5'])

    A=df1+df2
    print(A)


if __name__=="__main__":
    #operaciones()
    op_dataframe()