# usr/bin/env python3
import pandas as pd 
import sys
import matplotlib.pyplot as plt

def readExcel(url):
    data= pd.ExcelFile(url)
    print(data.sheet_names)
    data_gender= data.parse('Paciente',skiprows=0)#skipfooter=0,names=[)
    data_gender.set_index('idPais',inplace=True)
    data_gender.plot()
    plt.show()
    print(data_gender)
    print(type(data))
    print(type(data_gender))
if __name__=="__main__":
    if len(sys.argv)<2:
        print("Ingrese una <PATH> relativa")
        exit(0)
    try:
        readExcel(sys.argv[1])
    except Exception as e:
        print(e)