'''' Nombre completo: NADIA IVANA DASZCZUK'''

from data_stark import lista_personajes
import re


#Punto A
def personajes_no_binarios():

    '''Imprime personajes No Binarios'''

    contador_nb = 0

    for personaje in lista_personajes:

        if personaje['genero'] == 'NB':
            contador_nb += 1
            print(f"El personaje no binario es: {personaje['nombre']}")
    
    if contador_nb == 0:
        print("No se encontraron personajes no binarios")


#Punto B y C
def maxima_altura_generos (genero:str):

    '''Indica el personaje con altura máxima según género ingresado'''
    contador = 0
    max_altura = None
    for personaje in lista_personajes:
        if genero == personaje["genero"]:
            contador += 1
            altura_float = float(personaje["altura"])
            if max_altura == None or max_altura < altura_float:
                max_altura = altura_float
                nombre_maximo_altura = personaje["nombre"]
    if contador > 0 :
        print(f"El personaje más alto es {nombre_maximo_altura}")
    else: 
        print(f"No se encontraron personajes con ese género")
    
    return nombre_maximo_altura


#Punto D y E
def minimo_fuerza_genero (genero):

    '''Indica el personaje con fuerza mínima según género ingresado'''

    min_fuerza = None
    contador = 0

    for personaje in lista_personajes:

        if genero == personaje["genero"]:
            contador += 1
            fuerza_int = int(personaje["fuerza"])
            if min_fuerza == None or min_fuerza > fuerza_int:
                min_fuerza = fuerza_int
                nombre_min_fuerza = personaje['nombre']
    if contador > 0 :
        print(f"El personaje más débil es {nombre_min_fuerza}")
    else: 
        print(f"No se encontraron personajes con ese género")
    
    
#Punto F
def promedio_fuerza_nb ():

    ''' Promedio de fuerza de personajes no binarios
    MODIFICAR EN TP'''

    acumulador_fuerza_nb = 0
    cantidad_nb = 0

    for personaje in lista_personajes:
        fuerza_int = int(personaje['fuerza'])

        if personaje['genero'] == "NB":
            acumulador_fuerza_nb = acumulador_fuerza_nb + fuerza_int
            cantidad_nb += 1
    
    if cantidad_nb > 0:
        promedio_fuerza = acumulador_fuerza_nb / cantidad_nb
        return promedio_fuerza
    else:
        return 0


#Punto G
def cantidad_color_de_ojos ():

    ''' Cantidad de personajes por color de ojos'''
    dicc_color_ojos = {}
    for personaje in lista_personajes:
        color = personaje["color_ojos"].upper()
        if color in dicc_color_ojos:
            dicc_color_ojos[color] += 1
        else:
            dicc_color_ojos[color] = 1

    return dicc_color_ojos

#Punto H
def cantidad_color_de_pelo ():

    '''Cantidad de personajes por color de pelo'''
    dicc_color_pelo = {}
    for personaje in lista_personajes:
        color = personaje["color_pelo"].upper()
        if color in dicc_color_pelo:
            dicc_color_pelo[color] += 1
        else:
            dicc_color_pelo[color] = 1
    
    return dicc_color_pelo
        


    
#PUNTO I 

def agrupar_personajes_por_color_ojos (): 

    '''Listar personajes por color de ojos'''

    pers_color_ojos = {}
    for personaje in lista_personajes:
        color_actual = personaje["color_ojos"].upper()
        if color_actual in pers_color_ojos:
            pers_color_ojos[color_actual].append(personaje["nombre"])
        else:
            pers_color_ojos[color_actual] = [personaje["nombre"]]
    print("Personajes de Marvel agrupados por color de ojos:")
    for color_actual, lista_pers in pers_color_ojos.items():
        print(f"---- {color_actual} ----")
        for nombre in lista_pers:
            print(nombre)

#Punto J
def agrupar_personajes_por_inteligencia ():

    '''Listar personajes por tipo de inteligencia'''

    personajes_por_inteligencia = {}
    personaje_no_descripto = None
    for personaje in lista_personajes:
        if personaje["inteligencia"] == "":
            personaje_no_descripto = personaje["nombre"]
            print(f"Hay un personaje que no tiene descripta su inteligencia, es: {personaje_no_descripto}")
        else:    
            inteligencia_actual = personaje["inteligencia"].upper()
            if inteligencia_actual in personajes_por_inteligencia:
                personajes_por_inteligencia[inteligencia_actual].append(personaje["nombre"])
            else:
                personajes_por_inteligencia[inteligencia_actual] = [personaje["nombre"]]
    
    print("Personajes de Marvel agrupados por inteligencia:")
    for inteligencia_actual, lista_pers in personajes_por_inteligencia.items():
        print(f"---- {inteligencia_actual} ----")
        for nombre in lista_pers:
            print(nombre)











''' FUNCIONES TP NUMERO 3'''


def verificar_si_numero(cadena_txt):
    confirmar_num = False

    sin_punto = cadena_txt.replace(".", "")
    
    confirmar_num = sin_punto.isdigit()
    
    return confirmar_num
    

def stark_normalizar_datos_tp_3(lista:list) -> bool:

    ''' Normaliza datos de una lista, si es un string que contiene números los castea a entero o a float según corresponda'''

    normalilizacion = False

    if len(lista) == 0:
        return normalizacion  
    
    for personaje in lista:

        for clave, valor in personaje.items():

            if clave in personaje and type(valor) != int and type(valor) != float:
            
                if re.search(r'^[0-9]+$', valor):
                    personaje[clave] = int(valor)
                    normalizacion = True
                elif re.search(r'^[0-9]+\.[0-9]+$', valor):
                    personaje[clave] = float(valor)
                    normalizacion = True
            else: 
                normalizacion = False
        
    return normalizacion    

    
def obtener_dato(diccionario:dict, clave:str) -> bool:
    ''' Obtiene el dato dentro de la clave'''
    if len(diccionario) < 0:
        return False
    
    if diccionario:
            if clave in diccionario:
                dato = diccionario[clave]
            else:
                dato = False
    
    return dato         



def obtener_nombre(diccionario:dict, clave:str):
    '''Obtiene contenido clave de personaje'''

    if len(diccionario) < 0:
        return False
    
    clave_valor= obtener_dato(diccionario, clave="nombre")
    
    if clave_valor is not False:
        mensaje = f"{clave}: {clave_valor}"
    else:
        mensaje = False
    
    return mensaje

def obtener_nombre_y_dato(diccionario:dict, clave:str) -> str:
    '''Obtiene el nombre y el dato de la clave que se solicite'''
    if len(diccionario) <= 0:
        return False
    
    nombre = obtener_nombre(diccionario, clave="nombre")

    if nombre is not False:
        dato = obtener_dato(diccionario, clave)

        if dato is not False:
            mensaje = f"{nombre} | {clave} : {dato}"
            return mensaje
    return False


def obtener_maximo(lista:list, clave:str):
    '''Obtiene el máximo de los tipos de clave que son int o float'''
    maximo = lista[0][clave]
    
    if len(lista) == 0:
        return False
       
    for personaje in lista:
        
        if clave in personaje:
            if type(personaje[clave]) == int or type(personaje[clave]) == float:
                valor_actual = personaje[clave]
                if maximo < valor_actual:
                    maximo = valor_actual
            else:
                return False
    
    return maximo



def obtener_minimo(lista:list, clave:str):
    '''Obtiene el mínimo de los tipos de clave que son int o float'''
    minimo = lista[0][clave]
    
    if len(lista) == 0:
        return False
       
    for personaje in lista:
        
        if clave in personaje:
            if type(personaje[clave]) == int or type(personaje[clave]) == float:
                valor_actual = personaje[clave]
                if minimo > valor_actual:
                    minimo = valor_actual
            else:
                return False
    
    return minimo

def obtener_cantidad(lista:list, valor:str or float or int, clave:str):
    '''Obtiene una lista con el diccionario de los personajes que cumplen la condición solicitada'''
    lista_condicion = []

    for personaje in lista:
        valor_personaje = obtener_dato(personaje, clave)
        

        if valor_personaje == valor:
            lista_condicion.append(personaje)

    if len(lista_condicion) > 0:
        return lista_condicion
    else:
        return False       

def stark_imprimir_personajes(lista:list):
    """Imprime los personajes que forman parte de la lista solicitada"""
    if lista == 0:
        return False
    
    for personaje in lista:
        print("Información del personaje:")

        for clave, valor in personaje.items():
            print(f"{clave.capitalize()} : {valor}")

        print("--------------------------")

def sumar_dato_heroe (lista:list, clave:str):
    '''Suma el valor de la clave solicitada'''
    suma_total = 0
    
    if len(lista) <= 0:
        return False
    
    for personaje in lista:

        if clave in personaje:

            suma_total += personaje[clave]

    return suma_total
    

def dividir (dividendo:int or float or str, divisor:int or float):
    '''Función para dividir'''
    if divisor == 0:
        return False
    
    else:
        total_division = dividendo / divisor
    
    return total_division

def contar_heroes_con_valor(lista:list, clave:str, valor):
    '''Contar heroes según valor que se asigne'''
    cantidad = 0

    for personaje in lista:
        if clave in personaje and personaje[clave] == valor:
            cantidad += 1

    return cantidad

def contar_heroes_con_clave(lista:list, clave:str):
    '''Contar heroes según clave'''
    cantidad = 0

    for personaje in lista:
        if clave in personaje:
            cantidad += 1

    return cantidad

def calcular_promedio (lista: list, clave: str):
    ''' Calcula promedio'''
    cantidad_personajes = contar_heroes_con_clave(lista_personajes, clave)
    suma_personajes = sumar_dato_heroe(lista, clave)
    

    if cantidad_personajes > 0:
        promedio = suma_personajes / cantidad_personajes
        return promedio
    else:
        return 0

def mostrar_promedio_dato(lista:list, clave:str):
    '''Muestra promedio'''

    if len(lista) == 0 :
        return False
    
    for personaje in lista:

        if clave in personaje:
            if type(personaje[clave]) == int or type(personaje[clave]) == float:
                respuesta = calcular_promedio(lista, clave)
            else:
                respuesta = False
    return respuesta

def imprimir_menu_tp_3(cadena:str):
    print(cadena)

def validar_entero (numero:str):
    corroborar_numero = False
    corroborar_numero = numero.isdigit()

    if corroborar_numero == True:
        return corroborar_numero
    
    return corroborar_numero


def stark_menu_principal_tp_3():

    menu = imprimir_menu_tp_3(cadena="1. Normalizar datos\n2- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB\n3- Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n4- Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n5- Recorrer la lista y determinar cuál es el superhéroe más débil de género M\n6- Recorrer la lista y determinar cuál es el superhéroe más débil de género NB\n7- Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB\n8- Determinar cuántos superhéroes tienen cada tipo de color de ojos\n9- Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n10- Listar todos los superhéroes agrupados por color de ojos.\n11- Listar todos los superhéroes agrupados por tipo de inteligencia\n12- Seleccione para salir del sistema")

    numero = input("Ingrese un número: ")
    numero_validado = validar_entero(numero)

    if numero_validado == True:
        numero_int = int(numero)
        
    else:
        numero_int = False
        
    return numero_int












''' Funciones trabajo práctico n° 4'''

def extraer_iniciales(nombre_heroe:str):
    ''' Obtiene las iniciales del nombre del heroe separadas por punto y con mayúscula'''
    if not nombre_heroe:
        return "N/A"
    
    nombre_heroe = nombre_heroe.replace("-", " ")

    palabras_nombre = nombre_heroe.split()

    iniciales = []

    for palabra in palabras_nombre:

        if palabra.lower() == "the":
            continue 

        inicial = palabra[0].upper()

        iniciales.append(inicial)

        iniciales_nombre = ".".join(iniciales)

    return iniciales_nombre  


def definir_iniciales_nombre (heroe:dict) -> bool:
    ''' Crea clave "iniciales" en diccionario y agrega las iniciales, si no es diccionario o no esta la clave devuelve False'''

    if type(heroe) != dict:
        return False
    
    if "nombre" not in heroe:
        return False
    
    nombre_heroe = heroe["nombre"]

    iniciales = extraer_iniciales(nombre_heroe)

    heroe["iniciales"] = iniciales

    return True

def agregar_iniciales_nombre(lista:list) -> bool:
    ''' Agrega iniciales del nombre al diccionario, si no es una lista o la lista esta vacía devuelve False'''

    if type(lista) != list and len(lista) == 0:
        print("error")
        return False
    
    for diccionario in lista:

        resultado = definir_iniciales_nombre(diccionario)

        if not resultado:
            print("El origen de los datos no tiene el formato correcto")
            return False

    return True

def stark_imprimir_nombres_con_iniciales(lista:list):
    ''' Imprime nombre de heroes con las iniciales. '''
    if type(lista) != list or len(lista) == 0:
        print("Error")

    resultado = agregar_iniciales_nombre(lista)

    if not resultado:
        print("error")
        return
    
    for diccionario in lista:
        nombre = diccionario["nombre"]
        iniciales = diccionario["iniciales"]
        print(f"*{nombre} ({iniciales})")

def generar_codigo_heroe (id_heroe:int, genero:str):
    '''Genera códigos para cada heroe'''
    if type(id_heroe) != int:
        return "N/A"
    
    genero_mayusculas = genero.upper()

    if genero_mayusculas not in ("M", "F", "NB"):
        return "N/A"
    
    id_heroe_str = str(id_heroe)

    codigo = (f"{genero_mayusculas}-{id_heroe_str.zfill(8)}")

    if len(codigo) <= 10:
        return codigo
    else:
        return "N/A"

def agregar_codigo_heroe (heroe:dict, id_heroe:int):
    '''Agrega la clave código al diccionario'''
    if type(heroe) != dict or not heroe:
        return False
    
    codigo = generar_codigo_heroe(id_heroe, heroe.get("genero"))

    if len(codigo) != 10:
        print("error")
        return False

    heroe["codigo"] = codigo
    return True

def stark_generar_codigos_heroes(lista:list):
    '''Agrega código a cada heroe '''
    if type(lista) != list or len(lista) == 0:
        print("El origen de los datos no tiene el formato correcto")

    for heroe in lista:
        if type(heroe) != dict:
            print("El origen de los datos no tiene el formato correcto")
        if "genero" not in heroe:
            print("El origen de los datos no tiene el formato correcto")
    
    id_heroe = 1
    cantidad_codigos = 0
    for heroe in lista:
        agregar_codigo = agregar_codigo_heroe(heroe, id_heroe)
        id_heroe += 1
        cantidad_codigos +=1 
    
    print(f"Se asignaron {cantidad_codigos} de códigos.\n* El código del primer heroe es {lista[0]['codigo']}\n* El código del último heroe es {lista_personajes[23]['codigo']}")

def sanitizar_entero(numero_str:str) -> int:
    ''' Convierte número string a entero, devuelve int '''
    numero_str = numero_str.strip()
    
    if not numero_str.isdigit():
        return -1

    elif int(numero_str) < 0:
        return -2
    
    numero_int = int(numero_str)

    if type(numero_int) != int:
        return -3
    else:
        return numero_int

    


def sanitizar_flotante(numero_str:str) -> float:
    ''' Convierte numero flotante string a flotante, devuelve float'''
    numero_str = numero_str.strip()

    patron = r'^-?\d+\.\d+$'
    busqueda = re.match(patron, numero_str)
    if busqueda:
        numero_float = float(numero_str)
        if numero_float < 0:
            return -2
        return numero_float
    elif busqueda == None:
        return -1
    else:
        return -3
    

def sanitizar_string(valor_str:str, valor_por_defecto="-"): 
    
    valor_str = valor_str.strip()

    valor_str = re.sub(r'/', ' ', valor_str)

    if re.search(r'[0-9]+', valor_str):
        return "N/A"   
    
    if not valor_str and valor_por_defecto:
        valor_por_defecto = valor_por_defecto.lower()
        return valor_por_defecto
    else:
        valor_str = valor_str.lower()
        return valor_str

def sanitizar_dato(heroe:dict, clave:str, tipo_dato:str) -> bool: 

    tipo_dato = tipo_dato.lower()

    if tipo_dato not in ['string', 'entero', 'flotante']:
        print("Tipo de dato no reconocido")
        return False
    
    elif clave not in heroe:
        print("La clave especificada no existe en el héroe")
        return False
    
    valor = heroe[clave]

    match tipo_dato:
        case 'string':
            heroe[clave] = sanitizar_string(valor)
        
        case 'flotante':
            heroe[clave] = sanitizar_flotante(valor)
        
        case _: 
            heroe[clave] = sanitizar_entero(valor)
    return True

def stark_normalizar_datos (lista:list):
    ''' Normaliza los datos string a los valores que corresponde. Int, float o str'''
    if len(lista) <= 0:
        print("Error la lista esta vacía.")
        return False
    
    for heroe in lista:
        for clave, valor in heroe.items():
            match clave: 
                case 'altura':
                    valor_sanitizado = sanitizar_dato(heroe, clave, tipo_dato="flotante")

                case 'peso':
                    valor_sanitizado = sanitizar_dato(heroe, clave, tipo_dato="flotante")

                case 'color_ojos':
                    valor_sanitizado = sanitizar_dato(heroe, clave, tipo_dato="string")

                case 'color_pelo':
                    valor_sanitizado = sanitizar_dato(heroe, clave, tipo_dato="string")

                case 'fuerza':
                    valor_sanitizado = sanitizar_dato(heroe, clave, tipo_dato="entero")

                case 'inteligencia':
                    valor_sanitizado = sanitizar_dato(heroe, clave, tipo_dato="string")
    return True
    
                    
def generar_indice_nombre(lista:list):
    '''Une todos los nombres en una lista'''
    if len(lista) <= 0:
        print("El origen de datos no contiene el formato correcto")
        return 
    indice_nombres = []

    for heroe in lista:

        if 'nombre' in heroe:
            nombre = heroe['nombre']
            palabras_nombre = nombre.split()
            for palabra in palabras_nombre:
                indice_nombres.append(palabra)
        else:
            print("El origen de datos no contiene el formato correcto") 
            return 
    return indice_nombres

def stark_imprimir_indice_nombre(lista:list):
    ''' Imprime lista con los nombres separados con guiones'''
    indice_nombres = generar_indice_nombre(lista)

    indice_guiones = '-'.join(indice_nombres)
    
    return indice_guiones

def convertir_cm_a_mtrs(valor_cm):
    '''Convierte centimetros a metros'''
    if type(valor_cm) == float and valor_cm >= 0:
        valor_mtrs = valor_cm / 100
        return valor_mtrs
    else:
        return -1

def generar_separador(patron, largo, imprimir:bool=True) -> str:
    '''Genera un separador para imprimir por pantalla'''
    if len(patron) < 1 or len(patron) > 2:
        return "N/A"
    
    if type(largo) != int:
        return "N/A"
    elif largo < 1 or largo > 235:
        return "N/A"
    
    separador = patron * largo

    if imprimir:
        print(separador)
        imprimir = False
        return separador
    else:
        return separador
def generar_encabezado(titulo:str)->str:
    '''Genera encabezado con separador y título, devuelve el separador junto con título'''
    if not titulo or type(titulo) != str:
        return "N/A"

    titulo_mayus = titulo.upper()

    separador_superior = generar_separador(patron="*", largo=179, imprimir=False)
    separador_inferior = generar_separador(patron="*", largo=179, imprimir=False)

    encabezado = (f"{separador_superior}\n{titulo_mayus}\n{separador_inferior}\n")
    return encabezado

def imprimir_ficha_heroe(heroe:dict):
    '''Imprime la ficha de cada heroe '''
    if type(heroe) != dict:
        print("El origen de datos no contiene el formato correcto")
        return 
    
    encabezado_principal = generar_encabezado(titulo="PRINCIPAL")
    print(encabezado_principal)

    if 'nombre' in heroe:
        nombre_heroe = heroe['nombre']
        iniciales = extraer_iniciales(heroe["nombre"])
        print(f"NOMBRE DEL HEROE: {nombre_heroe} ({iniciales})")

    if 'identidad' in heroe:
        identidad = heroe['identidad']
        print(f"IDENTIDAD SECRETA: {identidad}")
    
    if 'empresa' in heroe:
        consultora = heroe['empresa']
        print(f"CONSULTORA: {consultora}")
    
    if 'codigo' in heroe:
        codigo = heroe['codigo']
        print(f"CODIGO DE HEROE: {codigo}")
    else: 
        print("")
    
    encabezado_fisico = generar_encabezado(titulo="FISICO")
    print(encabezado_fisico)

    if 'altura' in heroe:
        valor_cm = heroe['altura']
        valor_mts = convertir_cm_a_mtrs(valor_cm)
        print(f"ALTURA: {valor_mts} mts.")

    if 'peso' in heroe:
        valor_peso = heroe['peso']
        print(f"PESO: {valor_peso} Kg.")
    
    if 'fuerza' in heroe:
        fuerza = heroe["fuerza"]
        print(f"FUERZA: {fuerza} N")
        print("")

    encabezado_señas_particulares = generar_encabezado(titulo="SEÑAS PARTICULARES")
    print(encabezado_señas_particulares)

    if 'color_ojos' in heroe: 
        color_ojos = sanitizar_string(valor_str=heroe['color_pelo'])
        color_ojos = color_ojos.capitalize()
        print(f"COLOR DE PELO: {color_ojos}")

    if 'color_pelo' in heroe: 
        color_pelo = sanitizar_string(valor_str=heroe['color_pelo'])
        color_pelo = color_pelo.capitalize()
        print(f"COLOR DE PELO: {color_pelo}")
        print("")

def stark_navegar_fichas(lista:list):
    if len(lista) <= 0:
        print("Error. La lista esta vacía.")
        return 
    
    flag = True
    indice_actual = 0

    while flag == True:

        imprimir_ficha_heroe(lista[indice_actual])

        opcion = input("[ 1 ] Ir a la izquierda.\n[ 2 ] Ir a la derecha\n[ S ] Salir\nIngrese una opción: ")

        if opcion == "1":
            indice_actual = (indice_actual - 1) % len(lista)
            print(indice_actual)
        elif opcion == "2":
            indice_actual = (indice_actual + 1) % len(lista)
            
        elif opcion.upper() == "S":
            flag = False
        
        else:
            print("Opción no valida. Ingrese una opción correcta")

def imprimir_menu_tp4():
    '''Imprime las opciones del menú'''
    menu = "1 - Imprimir la lista de nombres junto con sus iniciales\n2 - Generar códigos de héroes\n3 - Normalizar datos\n4 - Imprimir índice de nombres\n5 - Navegar fichas\nS - Salir"

    print(menu)

def stark_menu_principal_tp4() -> str:
    '''Le pide al usuario que ingrese una opción del menú, retorna la opción'''
    menu = imprimir_menu_tp4()

    opcion = input("Ingrese una opción:")

    return opcion

def stark_marvel_app_tp_4(lista):
    ''' Ejecuta las funciones para cumplir con las opciones'''
    flag = True
    while flag:
        opcion = stark_menu_principal_tp4()
        
        if opcion == "1":
                respuesta = stark_imprimir_nombres_con_iniciales(lista)
            
        elif opcion == "2":
                stark_generar_codigos_heroes(lista)
            
        elif opcion == "3":
            if stark_normalizar_datos(lista) == True:
                print("Los datos se encuentran normalizados")
            else:
                print("Error, verifique que los datos no se encuentren normalizados")
        elif opcion == "4":
                print(stark_imprimir_indice_nombre(lista))

        elif opcion == "5":
                stark_navegar_fichas(lista)

        elif opcion.upper() == "S": 
            print("Saliendo del sistema...")
            flag = False
        else:
            print("Opción incorrecta... ingrese una opción valida")




