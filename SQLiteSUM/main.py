from sqliteConnection import *

def main():
    #cargamos la conexion y las consultas
    connection=SQLite3Database.get_connection(r"Database\myDatabase.db")
    querys=load_querys(r'querys.json')
    print("[+] Lista de consultas cargadas correctamente")
    SQLite3Services.executeQuery(connection,querys)
    #finalizacion del programa
    print("Consultas existosas")
if __name__=="__main__":
    try:
         main()
    except Exception as e: 
        print("Excepcion: {0}".format(e))
        
    
    
        