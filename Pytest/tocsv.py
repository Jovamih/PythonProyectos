# /usr/bin/env python3

#(about). Este script convierte una tabla encontrada en fichero html a  formato CSV
#paa ello realizara los siguientes pasos

#(+). Construir una funcio que encuentre determinada palabra entre un conjunto de caracteres especificadas
    #ej. buscar entre 'a' y 'mn'-> 'la determinada tranr tmn': devuelve: 'nr t'

#1. Funcion que detecte el inicio y final  de una tabla  en codigo html, para que mas rendimiento en vez de
    #iterar linea por linea buscando ducho patron de busqueda
#2 funcion que identifique las columna sde una tabla html
#3 funcion que identifique las filas de una tabla html
#4 funcion principal que integre las demas funciones y escribba en fichero csv

import csv

def search_word(word=str(),start=str(),end=str()):
    first=word.find(start)
    if first!=-1:
        word=word[first+len(start):]
        last=word.find(end)
        if last!=-1:
            return word[:,last]
    return None
def search_advanced_word(word=str(),start=str(),end=str()):
    currency=list()
    while len(start)+len(end)<len(word):

        first=word.find(start)
        if first!=-1:
            word=word[first+len(start):]
            last=word.find(end)
            if last!=-1:
                currency.append(word[:last])
                word=word[last+len(end):]

            else: break
        else :
            break
    return currency

def search_advanced_modified(word=str(),start=str(),end=str()):
    
    lista=search_advanced_word(word,start,end)
    #print(lista)
    return [body[body.find(">")+1 :] for body in lista]
    


def main(path=str()):
    #os.chdir(os.path.dirname(path))
    filename=os.path.basename(path)
    filename=filename[:filename.rfind(os.path.extsep)]+"{0}.csv"
    with open(path,'r') as f:
        data=f.readlines()
    data=[line.strip() for line in data if line]
    texto="".join(data)
    #print(texto)
    #primeo buscamos las tablas
    tables=search_advanced_modified(texto,start='<table',end='</table>')
    print("{0} Tablas encontradas".format(len(tables)))
    for i,table in enumerate(tables):
        #creamos una lista de datos de cada fila
        datarows=list()
        #toda tabla tiene una cabezera y cuerpo
        
        #asi que primero obtenemos la cabezera y de ahi obtendremos el nombre de las columnas
        thead=search_advanced_word(table,start='<thead>',end='</thead>') #lista de cabezeras
        # como solo tiene una, obtenemos el primer elemento y obtenms las columnas
        columns=search_advanced_modified(thead[0],start='<th',end='</th>')
        print("\tT{0}: {1} Columnas encontradas".format(i+1,len(columns)))
        #datarows.append(columns)
        #ahora obtenemos el cuerpo
        
        tbody=search_advanced_word(table,start='<tbody>',end='</tbody>')
        print(len(tbody))
        #como solo tiene un cuerpo obtenemos el primer elemento y obtenemos las lista de filas
        rows=search_advanced_modified(tbody[0],start='<tr',end='</tr>')
        #ahora una vez obtenido la lista de filas obtendremos los elemento que corresponden
        #a cada columna
        print("\tT{0}: {1} Filas encontradas".format(i+1,len(rows)))
        for row in rows:
            #obtenemos los datos de cada fila
            data=search_advanced_modified(row,start='<td>',end='</td>')
            #y luego los agregamos
            datarows.append(data)

        csvdata=pd.DataFrame(datarows,columns=columns)
        csvdata.to_csv(filename.format(i))
        print('\tTabla {0} creada correctamente como {1}'.format(i+1,filename.format(i)))
        
if __name__=="__main__":
    import sys
    import os
    import pandas as pd
    
    if len(sys.argv)<2:
        print('<path> Parameter not found')
        sys.exit(0)
    
    if not os.path.isfile(sys.argv[1]):
        print("La ruta especificada hace alusion a un archivo que no existe")
        sys.exit(0)
    main(sys.argv[1])
    