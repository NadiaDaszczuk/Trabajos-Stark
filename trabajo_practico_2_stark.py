""""
Nombre completo : NADIA IVANA DASZCZUK

"""
from data_stark import lista_personajes
from funciones_stark import *

def mostrar_opciones ():

    print("MENÚ DESAFÍO STARK 2")
    print("Informes:")
    print("")
    print("A - Superhéroes género NO BINARIO")
    print("B - Superhéroe más alto de género FEMENINO")
    print("C - Superhéroe más alto de género MASCULINO")
    print("D - Superhéroe más débil de género MASCULINO")
    print("E - Superhéroe ás débil de género NO BINARIO")
    print("F - Fuerza promedio de los superhéroes de género NO BINARIO")
    print("G - Cantidad de superhéroes por color de ojos")
    print("H - Cantidad de superhéroes por color de pelo")
    print("I - Listado de personajes por color de ojos")
    print("J - Listado de personajes por inteligencia")
    print("X - Presiona X para salir.")


def elegir_opcion (opcion : int, bandera ):
    bandera = True
    match opcion :

        case "A":
            personajes_no_binarios()
            print("")

        case "B":
            genero = "F"
            maxima_altura_generos(genero)
            print("")
            
        case "C":
            genero = "M"
            maxima_altura_generos(genero)
            print("")

        case "D":
            genero = "M"
            minimo_fuerza_genero(genero)
            print("")

        case "E":
            genero = "NB"
            minimo_fuerza_genero(genero)
            print("")

        case "F":
            if promedio_fuerza_nb () == 0:
                print("No se encontraron personajes no binarios")
            else:
                print(f"El promedio de fuerza es {promedio_fuerza_nb()}")

        case "G":
            print(cantidad_color_de_ojos())
            print("")

        case "H":
            print(cantidad_color_de_pelo ())
            print("")

        case "I":
            agrupar_personajes_por_color_ojos ()
            print()

        case "J":
            agrupar_personajes_por_inteligencia ()
            print()
            
        case "X":
            print ("Saliendo del sistema...")
            print()
            bandera = False
        case _: 
            print(f"Opcion incorrecta.. Ingrese una opcion correcta")
            bandera  = True

    return bandera

bandera = True
while bandera == True :

    mostrar_opciones ()

    opcion = input("Ingrese una opcion: ")
    opcion_mayus = opcion.upper()
    print()
    print("Resultado: ")
    elegir_opcion (opcion_mayus,bandera)
    print("-------")

    if opcion_mayus == "X":
        bandera = False


cadena_menu = "1. Normalizar datos\n2- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB\n3- Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n4- Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n5- Recorrer la lista y determinar cuál es el superhéroe más débil de género M\n6- Recorrer la lista y determinar cuál es el superhéroe más débil de género NB\n7- Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB\n8- Determinar cuántos superhéroes tienen cada tipo de color de ojos\n9- Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n10- Listar todos los superhéroes agrupados por color de ojos.\n11- Listar todos los superhéroes agrupados por tipo de inteligencia"


"probando"