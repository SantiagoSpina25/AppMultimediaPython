import pymysql

connection = pymysql.connect(
    host="localhost", user="root", passwd="root", database="appmultimediahibernate_v3")


def elegirTabla():
    print("Sobre que tabla desea actuar?")
    eleccionTabla = 0

    while(eleccionTabla != 9):
        eleccionTabla = int(input(" 1.actor \n 2.episodio \n 3.genero \n 4.lista_de_vistos \n 5.pelicula \n 6.serie \n 7.temporada \n 8.usuario \n 9.Volver \n"))

        tabla = ""

        if eleccionTabla == 1:
            tabla = "actor"
        elif eleccionTabla == 2:
            tabla = "episodio"
        elif eleccionTabla == 3:
            tabla = "genero"
        elif eleccionTabla == 4:
            tabla = "lista_de_vistos"
        elif eleccionTabla == 5:
            tabla = "pelicula"
        elif eleccionTabla == 6:
            tabla = "serie"
        elif eleccionTabla == 7:
            tabla = "temporada"
        elif eleccionTabla == 8:
            tabla = "usuario"
        elif eleccionTabla == 9:
            print("Volviendo...")
        else:
            print("Elegí un numero del 1 al 9")
            print("\n")

        return tabla

def preguntarValores(tabla):
    if tabla == "actor":
        print("Los campos son: idActor, nombre, fechaNacimiento, nacionalidad")
    elif tabla == "episodio":
        print("Los campos son: idEpisodio, titulo, duracion, fecha_lanzamiento")
    elif tabla == "genero":
        print("Los campos son: idGenero, nombre, descripcion")
    elif tabla == "lista_de_vistos":
        print("Los campos son: idLista, titulo, tipo_contenido, fecha_agregado, estado")
    elif tabla == "pelicula":
        print("Los campos son: idPelicula, titulo, anio_lanzamiento, duracion, url_imagen")
    elif tabla == "serie":
        print("Los campos son: idSerie, titulo, anio_lanzamiento, num_temporadas, imagen_url")
    elif tabla == "temporada":
        print("Los campos son: idTemporada, numero_temporada, numero_episodios, fecha_lanzamiento")
    elif tabla == "usuario":
        print("Los campos son: idUsuario, nombre, correo, contrasena, tipo_suscripcion")

def realizarInsert():
    tabla = elegirTabla()

    if tabla != "":
        preguntarValores(tabla)
        valores = input("\nIngrese los valores: (ej: idActor, nombre) ")

        sql_ddl = "INSERT INTO " + tabla + " VALUES(null," + valores + ")"
        try:
            connection.cursor().execute(sql_ddl)
            print("Insercion exitosa")
            connection.commit()
        except Exception as e:
            print("Exception: ", e)

    


def realizarUpdate():
    tabla = elegirTabla()
    if tabla != "":
        preguntarValores(tabla)
        campo = input("\nIngrese el campo a actualizar: (ej: nombre = 'Santiago') ")
        condicion = input("Alguna condicion? ")

        sql_ddl = "UPDATE " + tabla + " SET " + campo + " " + condicion

        try:
            connection.cursor().execute(sql_ddl)
            print("Actualizacion exitosa")
            connection.commit()
        except Exception as e:
            print("Exception: ", e)
    


def realizarDelete():
    tabla = elegirTabla()

    if tabla != "":
        preguntarValores(tabla)
        condicion = input("Condicion para borrar? ")
        
        sql_ddl = "DELETE FROM " + tabla + " " + condicion
        
        try:
            connection.cursor().execute(sql_ddl)
            print("Borrado exitoso")
            connection.commit()
        except Exception as e:
            print("Exception: ", e)
    


def realizarSelect():
    tabla = elegirTabla()
    if tabla != "":

        preguntarValores(tabla)
        atributos = input("Seleccione atributos ")
        condicion = input("Alguna condicion para la consulta? ")
        sql_query = "SELECT " + atributos + " FROM " + tabla + " " + condicion

        try:
            cursor = connection.cursor()
            cursor.execute(sql_query)
            datos = cursor.fetchall()
            print("Datos encontrados: ", datos)

            connection.commit()
        except Exception as e:
            print("Exception: ", e)
    
