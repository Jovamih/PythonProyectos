from sqliteConnection import *
import sys,os 

if __name__=="__main__":
    pathDatabase=r"Database\myDatabase.db"
    conn=SQLite3Database.get_connection(pathDatabase)
    if not conn:
        sys.exit(0)
        #atendemos el servicio
    service=SQLite3Services(conn)
    #obtenemos la lista de querys
    pathQuerys=r"querys.json"
    queryList=load_querys(pathQuerys)
    print("[+] Lista de consultas crgadas correctamente")
    #iteramos sobre las listas para determinar las consultas
    #para consultas SELECT (porque devuelven resultados)
    print(" CONSULTAS SELECT ".center(30,"="))
    for query in queryList["querysSelect"]:
        print(">>>> {0}\n".format(query))
        resultRows=service.executeQuery(query)
        for row in resultRows:
            print(row)
        print("{0} Rows affected".format(len(resultRows)))
    #para los demas tipos de consultas
    print(" CONSULTAS INSERT,UPDATE,DELETE".center(40,"="))
    for query in queryList["querysNonSelect"]:
        print(">>>> {0}".format(query))
        rowcount=service.executeNonQuery(query)    
        print("{0} Rows affected".format(rowcount))
    
        