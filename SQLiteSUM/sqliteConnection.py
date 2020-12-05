import sqlite3
from sqlite3 import Error
import os
import json,sys
import subprocess 
"""
Preparamos el uso para la importacion de libreria de probablemente faltantes
"""
try:
    import prettytable
except ModuleNotFoundError:
    print("[*] Instalando el paquete 'prettytable'")
    subprocess.check_call([sys.executable,'-m','pip','install','prettytable'])
finally:
    from prettytable import PrettyTable 

#clase creda para tener la conexion a la base de datos lite
class SQLite3Database(object):
    
    @staticmethod
    def get_connection(name):
        """
        conexion a la base de datos sqlite3
        """
        connection=None
        if os.path.isfile(os.path.abspath(name)):
            try:
                connection=sqlite3.connect(name)
                print("[+] Conexion a Sqlite3 establecida")
            except Error:
                print("[-] No se pudo establecer conexion a la base de datos")
        else:
            print("[-] Base de datos no reconocida")
            
        return connection
    
class SQLite3Services(object):
    """
    Servicios de administracion de la base de datos
    """
    @staticmethod
    def executeQuery(connection,querys):
        """
        Recibe como parametro un lista de querys a evaluar
        """
        cursorObj=connection.cursor()
        for i,query in enumerate(querys):
            print("\nQuery {0} : {1}\n".format(i+1,query))
            if query.lstrip().upper().startswith('SELECT'): #verificamossi pertenece a un select
                cursorObj.execute(query)               #ejecutamos la consulta
                column_names=[tup_column[0] for tup_column in cursorObj.description]
                content_rows=cursorObj.fetchall()
                #creamos las tablas
                table=PrettyTable(column_names)
                table.add_rows(content_rows)
                print(table)
                print("{0} Rows affected".format(len(content_rows)))
            else:
                #para consultas diferentes de SELECT
                cursorObj.execute(query)
                print("{0} Rows affected".format(cursorObj.rowcount))
        #connection.commit()  #importante descomentar esto cuando el programa este listo
def load_querys(name):
    with open(name,mode='r') as f:
        fjson=json.load(f) 
    return fjson['querys']


        
    