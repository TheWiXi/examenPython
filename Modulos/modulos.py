import os
import Modulos.data as data


info=data.dataDownload()
listasimple=info[0]

def mainMenu():
    while True:
        os.system('cls')
        print("""Menu Principal BlockBuster:
            ___________________________________  
            1.Administrador de Generos.
            2.Administrador de Actores.
            3.Administrador de Formatos.
            4.Gestor de Informes.
            5.Gestor de Peliculas.
            6.Salir.
        
        """)
        try:
            op=int(input("Ingres una opcion: _"))
            if op==1:
                generosCrud()
            elif op==2:
                actoresCrud()
            elif op==3:
                formatosCrud()
            elif op==4:
                informes()
            elif op==5:
                peliculasCrud()
            elif op==6:
                print("Saliendo...")
                os.system('pause')
                break
            else:
                print("Ingrese una opcion valida...")
                os.system('pause')
        except ValueError:
            print("Ingrese una opcion valida...")
            os.system('pause')


def generosCrud():
    while True:
        os.system('cls')
        print("""GESTOR DE GENEROS:
            ___________________________
            1.Crear genero.
            2.Listar generos.
            3.Volver al menu principal.
        
        """)
        try:
            op=int(input("Ingres una opcion: _"))
            if op==1:
                crearGenero()
            elif op ==2:
                listarGeneros()
            elif op==3:
                print("Volviendo al menu principal...")
                os.system('pause')
                break
            else:
                print("Ingrese una opcion valida...")
                os.system('pause')
        except ValueError:
            print("Ingrese una opcion valida...")
            os.system('pause')


def crearGenero():
    try:
        genero={
            "ID":"G"+str(len(listasimple["Generos"])+1),
            "Nombre":str(input("Ingrese el nombre del genero: _")).capitalize().replace(" ","")
        }
        listasimple["Generos"].append(genero)
        print("Genero creado con exito !")
        data.dataUpload(info)   
    except ValueError:
        print("Ingrese una opcion valida...")
        os.system('pause')


def listarGeneros():
    print("  CODIGO  |  " + "   |   ".join(listasimple["Generos"][0].keys()))
    for index, diccionario in enumerate(listasimple["Generos"]):
        print(f"   {index+1}      |   " + "  |  ".join(str(valor)
              for valor in diccionario.values()))
    os.system('pause')


def actoresCrud():
    while True:
        os.system('cls')
        print("""GESTOR DE ACTORES:
            ____________________________
            1.Crear Actor.
            2.Listar Actores.
            3.Volver al menu principal.
        
        """)
        try:
            op=int(input("Ingres una opcion: _"))
            if op ==1:
                crearActor()
            elif op==2:
                listarActores()
            elif op==3:
                print("Volviendo al menu principal...")
                os.system('pause')
                break
            else:
                print("Ingrese una opcion valida...")
                os.system('pause')
        except ValueError:
            print("Ingrese una opcion valida...")
            os.system('pause')


def crearActor():
    try:
        nombre=str(input("Ingrese el nombre del Actor: _")).capitalize()
        print("""
            Rol que puede desempeñar el actor:
            1.Protagonista.
            2.Antagonista.
            3.Reparto
        """)
        op=int(input("Ingrese el numero correspondiente al rol:_ "))
        if op==1:
            rol="Protagonista"
        elif op==2:
            rol="Antagonista"
        elif op==3:
            rol="Reparto"
        else: input("Ingrese una opcion valida...") 
        actor={
            "ID":"A"+str(len(listasimple["Actores"])+1),
            "Nombre":nombre,
            "Rol":rol
        }
        listasimple["Actores"].append(actor)
        print("Genero creado con exito !")
        data.dataUpload(info)   
    except ValueError:
        print("Ingrese una opcion valida...")
        os.system('pause')


def listarActores():
    print("  CODIGO  |  " + "   |   ".join(listasimple["Actores"][0].keys()))
    for index, diccionario in enumerate(listasimple["Actores"]):
        print(f"   {index+1}      |   " + "  |  ".join(str(valor)
              for valor in diccionario.values()))
    os.system('pause')


def formatosCrud():
    while True:
        os.system('cls')
        print("""GESTOR DE FORMATOS:
            ____________________________
            1.Crear formato.
            2.Listar formatos.
            3.Volver al menu principal.
        
        """)
        try:
            op=int(input("Ingres una opcion: _"))
            if op==1:
                crearFormato()
            elif op==2:
                listarFormatos()
            elif op==3:
                print("Volviendo al menu principal...")
                os.system('pause')
                break
            else:
                print("Ingrese una opcion valida...")
                os.system('pause')
        except ValueError:
            print("Ingrese una opcion valida...")
            os.system('pause')


def crearFormato():
    try:
        formato={
            "ID":"F"+str(len(listasimple["Formatos"])+1),
            "Nombre":str(input("Ingrese el nombre del Formato: _")).capitalize(),
            "ValorPrestamo":int(input("Ingrese sin puntos ni comas el valor de prestamo:_ "))
        }
        listasimple["Formatos"].append(formato)
        print("Formato creado con exito !")
        data.dataUpload(info)   
    except ValueError:
        print("Ingrese una opcion valida...")
        os.system('pause')


def listarFormatos():
    print("  CODIGO  |  " + "   |   ".join(listasimple["Formatos"][0].keys()))
    for index, diccionario in enumerate(listasimple["Formatos"]):
        print(f"   {index+1}      |   " + "  |  ".join(str(valor)
              for valor in diccionario.values()))
    os.system('pause')


def peliculasCrud():
    while True:
        os.system('cls')
        print("""GESTOR DE PELICULAS:
            ____________________________
            1.Agregar pelicula.
            2.Editar pelicula.
            3.Eliminar pelicula.
            4.Buscar pelicula.
            5.Listar todas las peliculas.
            6.Volver al menu principal.
        
        """)
        try:
            op=int(input("Ingres una opcion: _"))
            if op ==1:
                crearPelicula()
            elif op ==2:
                editarPelicula()
            elif op ==3:
                eliminarPelicula()
            elif op ==4:
                listarPeliculasEsp()
            elif op ==5:
                listarPeliculas()
            elif op==6:
                print("Volviendo al menu principal...")
                os.system('pause')
                break
            else:
                print("Ingrese una opcion valida...")
                os.system('pause')
        except ValueError:
            print("Ingrese una opcion valida...")
            os.system('pause')


def crearPelicula():
    try:
        nombre=str(input("Ingrese el nombre de la pelicula:_ ")).capitalize()
        listarGeneros()
        op=int(input("Ingrese el codigo del genero:_ "))
        actores=[]
        for i, value in enumerate(listasimple["Generos"]):
            if (op-1)==i:
                genero=value
        sinopsis=str(input("Ingrese la sinopsis:_ "))
        duracion=int(input("Ingrese la duracion de la pelicula(En minutos):_ "))
        numActores=int(input("Ingrese el numero de actores a agregar:_ "))
        listarActores()
        for i in range(numActores):
            op=int(input("Ingrese el codigo del actor:_ "))
            for i, value in enumerate(listasimple["Actores"]):
                if (op-1)==i:
                    actores.append(value)

        pelicula={
            "ID":"P"+str(len(listasimple["Peliculas"])+1),
            "Nombre":nombre,
            "Genero":genero,
            "Sinopsis":sinopsis,
            "Duracion":duracion,
            "ActoresPrincipales":actores
        }
        listasimple["Peliculas"].append(pelicula)
        print("Pelicula creada con exito !")
        data.dataUpload(info)   
    except ValueError:
        print("Ingrese una opcion valida...")
        os.system('pause')


def editarPelicula():
    try:
        listarPeliculas()
        op=int(input("Ingresse el codigo de la pelicula:_ "))
        for i,value in enumerate(listasimple["Peliculas"]):
            if (op-1)==i:
                print("""
                Opciones a editar:
                    1.Nombre.
                    2.Genero.
                    3.Sinopsis.
                    4.Duracion.
                    5.Actores.
                    6.Cancelar
                """)
                opc=int(input("Ingrese la opcion a editar:_ "))
                if opc==1:
                    listasimple["Peliculas"][i]["Nombre"]=str(input("Ingrese el nombre:_ "))
                    data.dataUpload(info) 
                elif opc==2:
                    listarGeneros()
                    opgen=int(input("Ingrese el codigo del genero:_ "))
                    genero=[]
                    for i, value in enumerate(listasimple["Generos"]):
                        if (opgen-1)==i:
                            genero.append(value)
                    listasimple["Peliculas"][i]["Genero"]=genero
                    data.dataUpload(info) 
                elif opc==3:
                    listasimple["Peliculas"][i]["Sinopsis"]=str(input("Ingrese la Sinopsis:_ "))
                    data.dataUpload(info) 
                elif opc==4:
                    listasimple["Peliculas"][i]["Duracion"]=int(input("Ingrese la duracio(en minutos):_ "))
                    data.dataUpload(info) 
                elif opc==5:
                    actores=[]
                    numActores=int(input("Ingrese el numero de actores a agregar:_ "))
                    listarActores()
                    for i in range(numActores):
                        op=int(input("Ingrese el codigo del actor:_ "))
                        for i, value in enumerate(listasimple["Actores"]):
                            if (op-1)==i:
                                actores.append(value)
                    listasimple["Peliculas"][i]["Actores"]=actores
                    data.dataUpload(info) 
                elif opc==6:
                    print("Volviendo al menu principal...")
                    os.system('pause')
                    break
                else:
                    print("Ingrese una opcion valida...")
                    os.system('pause')
    except ValueError:
        print("Ingrese una opcion valida...")
        os.system('pause')
                

def eliminarPelicula():
    try:
        listarPeliculas()
        op=int(input("Ingrese el codigo de la pelicula a eliminar:_ "))
        for i, key in enumerate(listasimple["Peliculas"]):
            if i==(op-1):
                listasimple["Peliculas"].remove(listasimple["Peliculas"][op-1])
        data.dataUpload(info)
    except ValueError:
            print("Ingrese una opcion valida...")
            os.system('pause')


def listarPeliculas():
    print("  CODIGO  |  " + "   |   ".join(listasimple["Peliculas"][0].keys()))
    for index, diccionario in enumerate(listasimple["Peliculas"]):
        print(f"   {index+1}      |   " + "  |  ".join(str(valor)for valor in diccionario.values()))
    os.system('pause')


def informes():
    while True:
        os.system('cls')
        print("""Menu Principal BlockBuster:
            1.Listar las peliculas de un genero.
            2.Listar peliculas por Actor.
            3.Buscar pelicula y mostrar sinopsis y actores.
            4.Volver al menu principal.
        
        """)
        try:
            op=int(input("Ingres una opcion: _"))
            if op ==1:
                peliculasGenero()
            elif op ==2:
                peliculasActor()
            elif op ==3:
                pass
            elif op==4:
                print("Volviendo al menu principal...")
                os.system('pause')
                break
            else:
                print("Ingrese una opcion valida...")
                os.system('pause')
        except ValueError:
            print("Ingrese una opcion valida...")
            os.system('pause')


def peliculasGenero():
    try:
        listarGeneros()
        gen=int(input("Ingrese el codigo del genero:_ "))
        print("  CODIGO  |  " + "   |   ".join(listasimple["Peliculas"][0].keys()))
        for i,value in enumerate(listasimple["Generos"]):
            if (gen-1)==i:
                genero=value
                for index,valor in enumerate(listasimple["Peliculas"]):
                    genpel=listasimple["Peliculas"][index]["Genero"]
                    if genero==genpel:
                        for index, diccionario in enumerate(listasimple["Peliculas"]):
                            print(f"   {index+1}      |   " + "  |  ".join(str(valor)
                                for valor in diccionario.values()))
                        os.system('pause')
    except ValueError:
        print("Ingrese una opcion valida...")
        os.system('pause')


def peliculasActor():
    try:
        listarActores()
        gen=int(input("Ingrese el codigo del actor:_ "))
        print("  CODIGO  |  " + "   |   ".join(listasimple["Peliculas"][0].keys()))
        for i,value in enumerate(listasimple["Actores"]):
            if (gen-1)==i:
                actor=value
                for index,valor in enumerate(listasimple["Peliculas"]):
                    actpel=listasimple["Peliculas"][index]["ActoresPrincipales"]
                    if actor in actpel:
                        for index, diccionario in enumerate(listasimple["Peliculas"]):
                            print(f"   {index+1}      |   " + "  |  ".join(str(valor)
                                for valor in diccionario.values()))
                        os.system('pause')
    except ValueError:
        print("Ingrese una opcion valida...")
        os.system('pause')

    
def listarPeliculasEsp():
    print("No se alcanzo a finalizar :(")
    os.system('pause')