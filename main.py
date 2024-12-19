import pymysql
from controlador import *

# Menu
eleccion = 0

while (eleccion != 5):
    eleccion = int(input("Que desea realizar 1.INSERT 2.UPDATE 3.DELETE 4.SELECT 5.SALIR \n"))
    if eleccion == 1:
        realizarInsert()
    elif eleccion == 2:
        realizarUpdate()
    elif eleccion == 3:
        realizarDelete()
    elif eleccion == 4:
        realizarSelect()
    elif eleccion == 5:
        print("Saliendo...")
    else:
        print("Elegí un numero del 1 al 5")
        print("\n")
    
connection.close()