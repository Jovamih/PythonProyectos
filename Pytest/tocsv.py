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
    os.chdir(os.path.dirname(path) if os.path.dirname(path) else '.' )
    filename=os.path.basename(path)
    filename=filename[:filename.rfind(os.path.extsep)]+"{0}.csv"
    with open(path,mode='r',encoding="cp437") as f:
        data=f.read()
    data=[line.strip() for line in data.split("\n") if line]
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
        #verificamos si tiene cabezeras (algunas asumen la cabezera con una fila mas (row) en el principio de la tabla  ignorando la sintaxis adecuada del nombrado de columnas)
        columns=list()
        if len(thead)!=0: #si posee una cabzera extraemos sus columnas, y si no pues se posigue a leer el cuerpo de la tabla(body)
            # como solo tiene una, obtenemos el primer elemento y obtenms las columnas
            columns=search_advanced_modified(thead[0],start='<th',end='</th>')
            
        print("\tT{0}: {1} Columnas encontradas".format(i+1,len(columns)))
        #datarows.append(columns)
        #ahora obtenemos el cuerpo
        
        tbody=search_advanced_word(table,start='<tbody>',end='</tbody>')
        #verificamos si posee un cuerpo (hay tablas que solo posse cabezera indiccando los nombres de columna, )
        rows=list()
        if len(tbody)!=0:
            #como solo tiene un cuerpo obtenemos el primer elemento y obtenemos las lista de filas
            rows=search_advanced_modified(tbody[0],start='<tr',end='</tr>')
            #ahora una vez obtenido la lista de filas obtendremos los elemento que corresponden
            #a cada columna
        print("\tT{0}: {1} Filas encontradas".format(i+1,len(rows)))
        #si no hay rows, el siguinete for se omitirá
        for count,row in enumerate(rows):
            #obtenemos los datos de cada fila
            data=search_advanced_modified(row,start='<td>',end='</td>')
            #y luego los agregamos
            datarows.append(data)
            print("\r\t\t{0} filas leidas".format(count+1),end="")
        #llego el momento de guardar los datos
        #si una columna esta vacia se le asigna None al momento de incluirlo en el dataFrame de Pandas
        csvdata=pd.DataFrame(datarows,columns=columns if len(columns)!=0 else None)
        #se guarda el DataFrame en una ruta especiffica
        csvdata.to_csv(filename.format(i))
        print('\n\tTabla {0} creada correctamente como {1}'.format(i+1,filename.format(i)))
        
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
    try:
        main(sys.argv[1])
    except Exception as e:
        print(e,file=sys.stderr)
    