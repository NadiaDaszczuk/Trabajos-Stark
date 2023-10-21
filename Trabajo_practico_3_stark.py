from funciones_stark import *
from data_stark import lista_personajes

def stark_marvel_app_tp_3 (lista):
    datos_normarlizados = False
    numero = stark_menu_principal_tp_3()
    bandera = True
    while  bandera == True or numero == False:
        numero = stark_menu_principal_tp_3()
        if numero != 1 and not datos_normarlizados:
            print("-----------")
            print("Error debe normalizar los datos primero")
            print("-----------")
        else:
            match numero :

                case 1:
                    resultado_normalizacion = stark_normalizar_datos_tp_3(lista_personajes)
                    if resultado_normalizacion == True:
                        print("-----------")
                        print("Datos Normalizados")
                        print("-----------")
                        datos_normarlizados = True
                    else:
                        print("-----------")
                        print("“Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente”")
                        print("-----------")
                    
                case 2:
                    nb_encontrados = False 

                    for personaje in lista_personajes:
                        genero = obtener_dato(personaje, "genero")
                        if genero == "NB":
                            nombre = obtener_dato(personaje, "nombre")
                            if nombre:
                                print("-----------")
                                print(f"Nombre: {nombre}")
                                print("-----------")
                                nb_encontrados = True
                        else:
                            nb_encontrados = False
            
                    if nb_encontrados == False:
                        print("-----------")
                        print("No se encontraron personajes no binarios")
                        print("-----------")
                    
                    

                case 3:
                    lista_femeninos = obtener_cantidad(lista_personajes, clave="genero", valor="F")
                    max_altura = obtener_maximo(lista_femeninos, clave="altura")
                    lista = obtener_cantidad(lista_femeninos, clave="altura", valor=max_altura)
                    print("-----------")
                    print(f"Los datos del femenino más alto son:")
                    mensaje= stark_imprimir_personajes(lista)
                    
                    

                case 4:
                    lista_masculinos = obtener_cantidad(lista_personajes, clave="genero", valor="M")
                    max_altura = obtener_maximo(lista_masculinos, clave="altura")
                    lista = obtener_cantidad(lista_masculinos, clave="altura", valor=max_altura)
                    print("-----------")
                    mensaje= stark_imprimir_personajes(lista)
                    print("-----------")
                    


                case 5:
                    
                    lista_masculinos = obtener_cantidad(lista_personajes, clave="genero", valor="M")
                    min_fuerza = obtener_minimo(lista_masculinos, clave="fuerza")
                    lista = obtener_cantidad(lista_masculinos, clave="fuerza", valor=min_fuerza)
                    print("-----------")
                    mensaje= stark_imprimir_personajes(lista)
                    print("-----------")
                   


                case 6:
                    
                    lista_nb = obtener_cantidad(lista_personajes, clave="genero", valor="NB")
                    if lista_nb != False:
                        min_fuerza = obtener_minimo(lista_nb, clave="fuerza")
                        lista= obtener_cantidad(lista_nb, clave="fuerza", valor=min_fuerza)
                        mensaje= stark_imprimir_personajes(lista)
                    else:
                        mensaje = "No se encontraron personajes no binarios"
                    print("-----------")
                    print(mensaje)
                    print("-----------")

                case 7:
                    
                    for personaje in lista_personajes:
                        lista_nb = obtener_cantidad(lista_personajes, clave="genero", valor="NB")
                    if lista_nb != False: 
                        fuerza_nb = sumar_dato_heroe(lista_nb, clave="fuerza")
                        promedio_fuerza_no_binario = calcular_promedio(lista_nb, clave="fuerza")
                        mostrar_promedio = mostrar_promedio_dato(lista_nb, clave="fuerza")
                    else:
                        print("-----------")
                        print("No se encontraron personajes no binarios")
                        print("-----------")
                    
                    

                case 8:
                    clave = "color_ojos"
                    for personaje in lista_personajes:
                        tipo_ojos = set(personaje[clave] for personaje in lista_personajes)

                    for ojo in tipo_ojos:
                        for personaje in lista_personajes:
                            if personaje[clave] == ojo:
                                cantidad = contar_heroes_con_valor(lista_personajes, clave, valor=ojo)
                        print(f"Tipo de ojo {ojo} | Cantidad: {cantidad} ")
                        print("-----------")
                    
                    
                        
                case 9:
                    clave = "color_pelo"
                    for personaje in lista_personajes:
                        tipo_pelo = set(personaje[clave] for personaje in lista_personajes)

                    for pelo in tipo_pelo:
                        for personaje in lista_personajes:
                            if personaje[clave] == pelo:
                                cantidad = contar_heroes_con_valor(lista_personajes, clave, valor=pelo)
                        print(f"Tipo de pelo {pelo} | Cantidad: {cantidad} ")
                        print("-----------")
                    
                    
                    
                case 10:
                    clave = "color_ojos"

                    for personaje in lista_personajes:
                        tipo_ojo = set(personaje[clave] for personaje in lista_personajes)

                    for ojo in tipo_ojo:
                        print("-----------")
                        print(f"-----{ojo}:-----")
                        print("")
                        for personaje in lista_personajes:
                            if personaje[clave] == ojo:
                                print(obtener_nombre_y_dato(personaje, clave))
                                print("")
        
                    
                    
                case 11:
                    clave = "inteligencia"

                    for personaje in lista_personajes:
                        tipo_inteligencia= set(personaje[clave] for personaje in lista_personajes)

                    for inteligencia in tipo_inteligencia:
                        print("-----------")
                        print(f"-----{inteligencia}:-----")
                        print("")
                        for personaje in lista_personajes:
                            if personaje[clave] == inteligencia:
                                print(obtener_nombre_y_dato(personaje, clave))
                                print("")
                    
                    
                case 12:
                    print("-----------")
                    print ("Saliendo del sistema...")
                    print("-----------")
                    break
                case _: 
                    print("-----------")
                    print(f"Opcion incorrecta.. Ingrese una opcion correcta")
                    print("-----------")

stark_marvel_app_tp_3(lista_personajes)