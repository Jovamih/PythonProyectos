import sqlite3
from sqlite3 import Error
import os
import json 
import subprocess 
"""
Preparamos el uso para la importacion de libreria de probablemente faltantes
"""
try:
    import prettytable
except ImportError:
    print("[*] Instalando el paquete 'prettytable'")
    subprocess.check_call([sys.executable,'-m','pip','install','prettytable','-y'])
finally:
    from prettytable import Prettytable 

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
    def __init__(self,connection):
        self.connection=connection
        self.cursorObj=self.connection.cursor()
    
    def executeQuery(self,query):
        self.cursorObj.execute(query)
        rows=self.cursorObj.fetchall()
        return rows 
        
    def executeNonQuery(self,query):
        self.cursorObj.execute(query)
        if self.cursorObj.rowcount<0:
            print("[-] La consulta no se realizo satisfactoriamente")
        else:
            # self.connection.commit()
             print("[+] Query exitoso")
        return self.cursorObj.rowcount
        
def load_querys(name):
    with open(name,mode='r') as f:
        fjson=json.load(f)
    return fjson


        
    