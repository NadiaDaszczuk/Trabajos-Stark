""""
Nombre completo : NADIA IVANA DASZCZUK

"""
from data_stark import lista_personajes

personaje_mas_fuerte = None
personaje_mas_bajo = None
contador_personajes_femeninos = 0
contador_personajes_masculinos = 0
acumulador_peso = 0
acumulador_fuerza_femeninos = 0

lista_personajes_fuertes = []
contador_personajes_fuertes = 0
        
for personaje in lista_personajes:    
    fuerza_int = int(personaje["fuerza"])
    altura_float = float(personaje["altura"])
    peso_float = float(personaje["peso"])
#B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)
    if personaje_mas_fuerte == None or personaje_mas_fuerte < fuerza_int:
        personaje_mas_fuerte = fuerza_int
        identidad_mas_fuerte = personaje["identidad"]
        peso_personaje_mas_fuerte = personaje["peso"]
    
        
#C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)   
    if personaje_mas_bajo == None or personaje_mas_bajo > altura_float:
        personaje_mas_bajo = altura_float
        nombre_personaje_mas_bajo = personaje["nombre"]
        identidad_personaje_mas_bajo = personaje["identidad"]

#D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)
    match personaje["genero"]:
        case "M":
            contador_personajes_masculinos += 1
            acumulador_peso = acumulador_peso + peso_float
        case "F":
            contador_personajes_femeninos += 1
            acumulador_fuerza_femeninos = acumulador_fuerza_femeninos + fuerza_int
#E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino
promedio_peso_personaje_masculinos = acumulador_peso / contador_personajes_masculinos
promedio_fuerza_femeninos = acumulador_fuerza_femeninos / contador_personajes_femeninos

for personaje in lista_personajes:
    fuerza_punto_d = int(personaje["fuerza"])
    peso_punto_d = float(personaje["peso"])
    
    if fuerza_punto_d == personaje_mas_fuerte and personaje["identidad"] != identidad_mas_fuerte and personaje["peso"] != personaje_mas_fuerte:
        lista_personajes_fuertes.append(personaje["identidad"])
        lista_personajes_fuertes.append(personaje["peso"])
        lista_personajes_fuertes.append(identidad_mas_fuerte)
        lista_personajes_fuertes.append(peso_personaje_mas_fuerte)
        contador_personajes_fuertes += 1
        mensaje_personaje_fuerte_1 = f"Se encontró más de un personaje con la misma fuerza, estos son: {lista_personajes_fuertes} su identidad y su peso respectivamente"
    elif contador_personajes_fuertes == 0:
        mensaje_personaje_fuerte_1 = f"El personaje con más fuerza es {identidad_mas_fuerte} y su peso es {peso_personaje_mas_fuerte} kg"

#Punto C)
mensaje_punto_c = (f"El nombre del personaje maás bajo es {nombre_personaje_mas_bajo}, su identidad es {identidad_personaje_mas_bajo} y su altura es {personaje_mas_bajo}")
#Punto D)
if contador_personajes_masculinos > 0:
    mensaje_punto_d = f"El peso promedio de los personajes masculinos es {promedio_peso_personaje_masculinos} kg."
else:
    mensaje_punto_d = f"No hay personajes masculinos"



#MENÚ
flag_menu = True

while flag_menu == True:
    print("Elija una opción:\nA-Recorre la lista imprimiendo todos los datos de cada superhéroe\nB-Recorre la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza\nC-Nombre e identidad del superhéroe más bajo\nD-Peso promedio de los superhéroes masculinos\nE-Nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino\nX- Salir del programa")

    opcion_elegida = input("Elija una opción: A - B - C - D - E - X: ") 
    opcion_elegida = opcion_elegida.upper()

    match (opcion_elegida):
        case 'A':
         for personaje in lista_personajes:
            print('')
            for descripcion in personaje:
                print(descripcion.upper(),':',personaje[descripcion])
            print('')   
    
        case 'B':
            print('')
            print(mensaje_personaje_fuerte_1)
            print('')

        case 'C':
            print('')
            print(mensaje_punto_c)
            print('')
        
        case 'D':
            print('')
            print(mensaje_punto_d)
            print('')

        case 'E':
            print('')
            for personaje in lista_personajes:
                fuerza_punto_e_int = int(personaje["fuerza"])
                peso_punto_e_float = float(personaje["peso"])
                if fuerza_punto_e_int > promedio_fuerza_femeninos:
                    print(f"Este personaje supera el promedio de la fuerza de los femeninos, el promedio de la fuerza de los femeninos es {promedio_fuerza_femeninos}:")
                    print(personaje["nombre"].upper()+":")
                    print(f"Su peso es: {peso_punto_e_float}")
                    print(f"Su fuerza es {fuerza_punto_e_int}")
                    print("")

        case 'X':
            print('')
            print("SALIENDO DEL PROGRAMA...")
            print('')
            flag_menu = False
        
        case _:
            print('')
            print("Opción incorrecta")
            print('')