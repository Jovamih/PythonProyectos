from sqlite_manager import *

def main():
    #cargamos la conexion y las consultas
    connection=SQLite3Database.get_connection("Database/myDatabase.db")
    querys=load_querys('Database/querys.txt')
    print("[+] Lista de consultas cargadas correctamente")
    SQLite3Services.executeQuery(connection,querys)
    #finalizacion del programa
    print("Consultas existosas")
if __name__=="__main__":
    try:
         main()
    except Exception as e: 
        print("Excepcion: {0}".format(e))
        
    
    
        