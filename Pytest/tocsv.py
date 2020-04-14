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

import pandas as pd

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
    print("point1")
    print("start {0}, end {1},words {2}".format(len(start),len(end),len(word)))
    while len(start)+len(end)<len(word):
        print("point2")
        first=word.find(start)
        if first!=-1:
            word=word[first+len(start):]
            print("Se encontro inicio")
            last=word.find(end)
            if last!=-1:
                currency.append(word[:last])
                word=word[last+len(end):]
                print("se encontro final")
            else: break
        else :
            break
    return currency

def search_advanced_modified(word=str(),start=str(),end=str()):
    
    lista=search_advanced_word(word,start,end)
    #print(lista)
    return [body[body.find(">")+1:] for body in lista]
    


def main(path=str()):
    with open(path,'r') as f:
        data=f.readlines()
    data=[line.strip() for line in data]
    texto="".join(data)
    #print(texto)
    #primeo buscamos las tablas
    tables=search_advanced_modified(texto,start='<table',end='</table>')
    print("{0} tablas".format(len(tables)))
    for i,table in enumerate(tables):
        #creamos una lista de datos de cada fila
        datarows=list()
        #toda tabla tiene una cabezera y cuerpo
        
        #asi que primero obtenemos la cabezera y de ahi obtendremos el nombre de las columnas
        thead=search_advanced_word(table,start='<thead>',end='</thead>') #lista de cabezeras
        # como solo tiene una, obtenemos el primer elemento y obtenms las columnas
        columns=search_advanced_word(thead[0],start='<th>',end='</th>')
        #ahora obtenemos el cuerpo
        
        tbody=search_advanced_word(table,start='<tbody>',end='</tbody>')
        #como solo tiene un cuerpo obtenemos el primer elemento y obtenemos las lista de filas
        rows=search_advanced_modified(tbody[0],start='<tr',end='</th>')
        #ahora una vez obtenido la lista de filas obtendremos los elemento que corresponden
        #a cada columna
        print("{} fila encontradas".format(len(rows)))
        for row in rows:
            #obtenemos los datos de cada fila
            data=search_advanced_word(row,start='<td>',end='</td>')
            #y luego los agregamos
            datarows.append(data)
        dataset=pd.DataFrame(datarows,columns=columns)
        dataset.to_csv('data {0}.csv'.format(i+1))
        print('Tabla {0} creada correctamente'.format(i+1))
        
if __name__=="__main__":
    import sys
    import os
    
    if len(sys.argv)<2:
        print('File or text not Found')
        sys.exit(0)
    
    if not os.path.isfile(sys.argv[1]):
        print("El archivo no existe")
        sys.exit(0)
    main(sys.argv[1])