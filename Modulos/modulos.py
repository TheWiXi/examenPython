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
        nombre=str(input("Ingrese el nombre del genero: _")).capitalize().replace(" ","")
        genero={
        "ID":"G"+str(len(listasimple["Generos"])+1),
            "Nombre":nombre
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
                pass
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
                pass
            elif op==2:
                pass
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


def peliculasCrud():
    while True:
        os.system('cls')
        print("""GESTOR DE PELICULAS:
            ____________________________
            1.Agregar pelicula.
            2.Editar pelicula.
            3.Eliminar pelicula.
            4.Eliminar Actor.
            5.Buscar pelicula.
            6.Listar todas las peliculas.
            7.Volver al menu principal.
        
        """)
        try:
            op=int(input("Ingres una opcion: _"))
            if op ==1:
                pass
            elif op ==2:
                pass
            elif op ==3:
                pass
            elif op ==4:
                pass
            elif op ==5:
                pass
            elif op ==6:
                pass
            elif op==7:
                print("Volviendo al menu principal...")
                os.system('pause')
                break
            else:
                print("Ingrese una opcion valida...")
                os.system('pause')
        except ValueError:
            print("Ingrese una opcion valida...")
            os.system('pause')


def informes():
    while True:
        os.system('cls')
        print("""Menu Principal BlockBuster:
            1.Listar las peliculas de un genero.
            2.Listar peliculas donde el protagonista sea Silvester Stallone.
            3.Buscar pelicula y mostrar sinopsis y actores.
            4.Volver al menu principal.
        
        """)
        try:
            op=int(input("Ingres una opcion: _"))
            if op ==1:
                pass
            elif op ==2:
                pass
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