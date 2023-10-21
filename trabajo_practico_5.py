import json
from funciones_stark import *
import re



def imprimir_menu_desafio_5():
    menu ="A. Nombre de cada superhéroe de género M\nB. Nombre de cada superhéroe de género F\nC. Superhéroe más alto de género M\nD. Superhéroe más alto de género F\nE. Superhéroe más bajo de género M\nF. Superhéroe más bajo de género F\nG. Altura promedio de los superhéroes de género M\nH. Altura promedio de los superhéroes de género F\nI. Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)\nJ. Cuántos superhéroes tienen cada tipo de color de ojos.\nK. Cuántos superhéroes tienen cada tipo de color de pelo.\nL. Cuántos superhéroes tienen cada tipo de inteligencia\nM. Superhéroes agrupados por color de ojos.\nN. Superhéroes agrupados por color de pelo.\nO. Superhéroes agrupados por tipo de inteligencia.\nS. SALIR"

    print(menu)

def stark_menu_principal_desafio_5():
    
    imprimir_menu_desafio_5()
    opcion = input("Ingrese una opción: ")
    if re.match(r'^[a-zA-Z]$', opcion):
        return opcion
    else:
        print("Error")
        return -1



def stark_marvel_app_5(lista:list):
    
    while True:
        letra = stark_menu_principal_desafio_5()
        if letra == -1:
            print("ERROR. Ingrese una opción correcta")
            letra = stark_menu_principal_desafio_5()
        letra = letra.upper()
        normalizacion = stark_normalizar_datos_tp_3(lista)
        match letra:
            case "A":
                stark_guardar_heroe_genero(lista, genero="M")
                
            case "B":
                stark_guardar_heroe_genero(lista, genero="F")
                
            case "C":
                stark_calcular_imprimir_guardar_heroe_genero(lista, clave="altura", calculo="maximo", genero="M" )
                
            case "D":
                stark_calcular_imprimir_guardar_heroe_genero(lista, clave="altura", calculo="maximo", genero="F")
                
            case "E":
                stark_calcular_imprimir_guardar_heroe_genero(lista, clave="altura", calculo="minimo", genero="M")
            case "F":
                stark_calcular_imprimir_guardar_heroe_genero(lista, clave="altura", calculo="minimo", genero="F")
                
            case "G":
                stark_calcular_imprimir_guardar_promedio_altura_genero(lista, clave="altura", genero="M")
            case "H":
                stark_calcular_imprimir_guardar_promedio_altura_genero(lista, clave="altura", genero="F")
            case "I":

                maximo_masc = calcular_max_min_dato_genero(lista, "altura", "maximo", "M")
                maximo_fem = calcular_max_min_dato_genero(lista, "altura", "maximo", "F")
                minimo_masc = calcular_max_min_dato_genero(lista, "altura", "minimo", "M")
                minimo_fem = calcular_max_min_dato_genero(lista, "altura", "maximo", "F")

                print(maximo_masc)
                print(maximo_fem)
                print(minimo_masc)
                print(minimo_fem)
            case "J":
                stark_calcular_cantidad_por_tipo(lista, clave="color_ojos")
            case "K":
                stark_calcular_cantidad_por_tipo(lista, clave="color_pelo")
            case "L":
                stark_calcular_cantidad_por_tipo(lista, clave="inteligencia")
            case "M":
                stark_listar_heroes_por_dato(lista, clave="color_ojos")
            case "N":
                stark_listar_heroes_por_dato(lista, clave="color_pelo")
            case "O":
                stark_listar_heroes_por_dato(lista, clave="inteligencia")
            case "S":
                print("Saliendo del sistema...")
                break
            case _:
                print("Opcion incorrecta. Ingrese una opción correcta")

def leer_archivo(nombre_archivo:str) -> list:

    with open(nombre_archivo, 'r') as archivo:
        lista_heroes = json.load(archivo)

        return lista_heroes["heroes"]

def guardar_archivo(nombre_archivo:str, contenido)->bool:
    '''Solicita nombre de archivo con formato correcto y el contenido. True en caso de que se haya creado y guardado el archivo y False en caso de error'''
    if re.match(r'^[a-zA-Z_]+\.[a-z]+$', nombre_archivo):
        with open(nombre_archivo, 'w+') as archivo:
            crear = archivo.write(contenido)
            if crear:
                print(f"El nombre del archivo es {nombre_archivo}")
                return True
            else:
                print(f"Hubo un error con el archivo {nombre_archivo}, vuelva a intentar")
                return False

def capitalizar_palabras(cadena:str)-> str:
    '''Permite capitalizar las palabras que se ingresen como párametro, de no ser de tipo STR retorna N/A, sino retorna la cadena con todas sus palabras capitalizadas'''
    if type(cadena) != str:
        return "N/A"

    palabras = cadena.split()

    
    cadena = " ".join(palabra.capitalize() for palabra in palabras)

    return cadena

def obtener_nombre_capitalizado(heroe:dict) -> str:
    '''Retorna el nombre capitalizado del diccionario que se ingrese por párametro'''
    if type(heroe) != dict or len(heroe) <= 0:
        return "N/A"
    
    if "nombre" in heroe:
        nombre_cap = capitalizar_palabras(heroe["nombre"])

    return nombre_cap

def obtener_nombre_y_dato_tp_5(heroe:dict, clave:str)->str:
    '''Obtiene el nombre y el dato de la clave que se solicite'''
    if len(heroe) <= 0:
        return False
    
    nombre = obtener_nombre_capitalizado(heroe)

    if nombre is not False:
        dato = heroe[clave]

    mensaje = f"{nombre} | {clave.capitalize()} : {dato}"
    
    return mensaje

## 2DA PARTE ##

def es_genero(heroe:dict, genero:str):
    '''Evalúa género, se indica por párametro un diccionario y un string género('M','N','NB') retorna True en caso de que coincida el genero del diccionario con el genero ingresado y False en caso de que no sea de tipo diccionario, que no tenga la clave genero, que no se encuentre entre 'M', 'F','NB' o que no coincida con el genero que se paso por párametro'''
    if type(heroe) != dict:
        return False
    
    if 'genero' not in heroe:
        return False
    
    genero = genero.upper()

    if genero not in ["M", "F", "NB"]:
        return False
    else:
        if heroe["genero"] == genero:
            return True
        else:
            return False

def stark_guardar_heroe_genero(lista:list, genero:str)->bool:
    '''Imprime los heroes que coinciden con el genero solicitado, además crea un archivo csv con sus nombres, recibe una lista y un string de género para comparar, retorna un booleano'''
    heroes_genero = []
    genero = genero.upper()
    if genero not in ['M', 'F', 'NB']:
        print("error 1")
        return False

    for heroe in lista:
        genero_heroe = es_genero(heroe, genero)
        if genero_heroe :
            nombre = obtener_nombre_capitalizado(heroe)
            print(obtener_nombre_y_dato_tp_5(heroe, clave='genero'))
            heroes_genero.append(nombre)
            heroes_final = ', '.join(heroes_genero)
        
    if genero == "M":
        nombre_archivo = "heroes_masculinos.csv"
        guardar_archivo(nombre_archivo, contenido=heroes_final)
        if guardar_archivo:
            return True
        else:
            return False

    elif genero == "F":
        nombre_archivo = "heroes_femeninos.csv"
        guardar_archivo(nombre_archivo, contenido=heroes_final)
        if guardar_archivo:
            return True
        else:
            return False

    else:
        nombre_archivo = "heroes_no_binarios.csv"
        guardar_archivo(nombre_archivo, contenido=heroes_final)
        if guardar_archivo:
            return True
        else:
            return False

def calcular_min_genero(lista:list, clave:str, genero:str)->str:
    ''' Permite obtener el nombre del minimo del género que se pase por párametro, debe ingresar la lista, la clave genero y el tipo de genero retorna un string con el nombre del heroe '''
    if type(lista) != list:
        return "N/A"
    
    genero = genero.upper()

    if genero not in ['M', 'F', 'NB']:
        return 'N/A'
    
    minimo = None

    for heroe in lista:

        if es_genero(heroe, genero) and ( minimo == None or minimo > heroe[clave]):
            minimo = heroe[clave]
            nombre_heroe = obtener_nombre_y_dato_tp_5(heroe, clave)
            
    if minimo != None:
        return nombre_heroe
    else:
        return None
    
def calcular_max_genero(lista:list, clave:str, genero:str)->str:
    ''' Permite obtener el nombre del maximo del género que se pase por párametro, debe ingresar la lista, la clave genero y el tipo de genero retorna un string con el nombre del heroe '''
    if type(lista) != list:
        return "N/A"
    
    genero = genero.upper()

    if genero not in ['M', 'F', 'NB']:
        return 'N/A'
    
    maximo = None

    for heroe in lista:

        if es_genero(heroe, genero) and ( maximo == None or maximo < heroe[clave]):
            maximo = heroe[clave]
            nombre_heroe = obtener_nombre_y_dato_tp_5(heroe, clave)

    if maximo != None:
        return nombre_heroe
    else:
        return None
    

def calcular_max_min_dato_genero(lista:list, clave:str, calculo:str, genero:str)->str:
    ''' Permite calcular el maximo y minimo de la clave que se ingrese por parametro. Se debe ingresar la lista a buscar, la clave, si es maximo o minimo y el genero. Retorna un string'''
    if type(lista) != list or len(lista) <= 0:
        return "N/A"
    
    genero = genero.upper()

    if genero not in ["M", "NB", "F"]:
        return "N/a"
    
    if calculo == "maximo":
        maximo = calcular_max_genero(lista, clave, genero)
        return maximo
    elif calculo == "minimo":
        minimo = calcular_min_genero(lista, clave, genero)
        return minimo
    else:
        mensaje = "Ingrese el dato correcto a buscar, maximo o minimo"
        return mensaje

def stark_calcular_imprimir_guardar_heroe_genero(lista:list, clave:str, calculo:str, genero:str)-> bool:
    '''Imprime el heroe máximo o mínimo del genero. Lo guarda en un archivo .csv'''
    if len(lista) <= 0:
        mensaje = "La lista se encuentra vacía"
        return mensaje
    
    calculo = calculo.lower()
    genero = genero.upper()
    
    if calculo not in ["maximo", "minimo"]:
        mensaje = "Ingrese un dato correcto.. maximo o minimo"
        return mensaje
    
    if genero not in ["M", "NB", "F"]:
        mensaje = "Error. Ingrese genero entre M / F / NB"

    heroe = calcular_max_min_dato_genero(lista, clave, calculo, genero)
    mensaje = f"{calculo.capitalize()} {clave.capitalize()}: {heroe}"
    print(mensaje)

    nombre_archivo = f"heroes_{calculo}_{clave}_{genero}.csv"
    guardar = guardar_archivo(nombre_archivo, mensaje)

    if guardar:
        return True
    else:
        return False


def sumar_dato_heroe_genero(lista:list, clave:str, genero:str)-> int:
    ''' Suma los datos de la clave contenida en cada héroe que se pase por párametro, del género que se indique por párametro, retorna un entero con la suma o un entero -1 que indica que no se pudo realizar la suma. Por párametro se indica la lista, la clave a contar y el género. '''
    suma = 0
    genero = genero.upper()

    if genero not in ["M", "F", "NB"]:
        return -1
    
    for heroe in lista:

        if type(heroe) == dict and heroe and 'genero' in heroe:
            genero_heroe = heroe['genero']
            if genero_heroe == genero and clave in heroe:
                dato = heroe[clave]
                suma += dato
        else:
            return -1
    
    if suma > 0:
        return suma 
    else:
        return -1
    
def cantidad_heroes_genero(lista:list, genero:str)->int:
    '''Indica la cantidad de personajes por género. Retorna la cantidad o 0 en caso de que no haya.'''
    cantidad = 0

    if len(lista) <= 0:
        return "N/A"
    
    genero = genero.upper()
    if genero not in ["M", "NB", "F"]:
        return "N/A"
    
    for heroe in lista:
        if genero == heroe["genero"]:
            cantidad += 1
    
    if cantidad > 0:
        return cantidad
    else:
        return 0

def calcular_promedio_genero(lista:list, clave:str, genero:str)->int:
    '''Calcula el promedio en base a la cantidad de personajes con el género indicado por párametro y la clave. Retorna el promedio o 0 en caso de que no haya podido realizar el promedio'''
    genero = genero.upper()
    if genero not in ["M", "F", "NB"]:
        return "N/A"
    
    cantidad_personajes = cantidad_heroes_genero(lista, genero)
    suma = sumar_dato_heroe_genero(lista, clave, genero)


    promedio = dividir(suma, cantidad_personajes)

    if promedio > 0:
        return promedio
    else:
        return 0
    
def stark_calcular_imprimir_guardar_promedio_altura_genero(lista:list, clave:str, genero:str)->bool:
    '''Calcula, imprime y guarda el promedio de altura en un archivo CSV. Por párametro indicar la lista, la clave altura y el género a buscar,Retorna True en caso de crearlo con éxito y False si hay algun error'''
    if not lista:
        print("Error, la lista esta vacía.")
        return False
    else:
        genero = genero.upper()
        if genero not in ["M", "NB", "F"]:
            return "N/A"
        promedio = calcular_promedio_genero(lista, clave, genero)
        if promedio:
            mensaje = f"{clave.capitalize()} promedio genero {genero}: {promedio}"
            print(mensaje)
        else:
            mensaje = "N/A"
    
    if mensaje != "N/A":
        nombre_archivo = f"heroes_promedio_{clave}_{genero}.csv"
        guardar = guardar_archivo(nombre_archivo, mensaje)

        if guardar:
            return True
        else:
            return False
    else:
        return False        

def calcular_cantidad_tipo(lista:list, clave:str)->bool:
    '''Calcula en un diccionario la cantidad de personajes según clave, la clave puede ser: color_ojos, color_pelo o inteligencia. Retorna el diccionario con las cantidades'''
    if not lista:
        dicc = {"Error": "La lista se encuentra vacia"}
        return dicc
    
    clave = clave.lower()

    if clave not in ["color_ojos", "color_pelo", "inteligencia"]:
        mensaje = "Error en el dato a buscar. Ingrese dato correcto"
        return mensaje
    
    dicc_color_ojos = {}
    for heroe in lista:
        color = capitalizar_palabras(heroe[clave])
        if color in dicc_color_ojos:
            dicc_color_ojos[color] += 1
        else:
            dicc_color_ojos[color] = 1

    return dicc_color_ojos

def guardar_cantidad_heroes(diccionario:dict, dato:str)->bool:
    ''' Imprime ségun dato la cantidad y variedad. El dato debe ser indicado por párametro junto con el diccionario y debe ser color_pelo, color_ojos o inteligencia. Retorna true en caso de que pueda guardar el archivo'''
    if not diccionario:
        return False
    
    if dato not in ["color_ojos", "color_pelo", "inteligencia"]:
        mensaje = "Error en el dato a buscar. Ingrese dato correcto"
        return mensaje
    mensaje = ""

    for variedad, cantidad in diccionario.items():
        mensaje += f"Caracteristica: {dato}, {variedad} - Cantidad de heroes: {cantidad}\n"
    
    print(mensaje)
    nombre_archivo = f"heroes_cantidad_{dato}.csv"
    guardar = guardar_archivo(nombre_archivo, mensaje)

    if guardar:
        return True

def stark_calcular_cantidad_por_tipo(lista:list, clave:str)->bool:
    ''' Guarda el diccionario con las cantidades de heroes que tengan el dato indicado por párametro. Si pudo guardar el archivo retorna True si hubo algún error retorna False'''
    diccionario = calcular_cantidad_tipo(lista, clave)
    guardar = guardar_cantidad_heroes(diccionario, clave)

    if guardar:
        return True
    else:
        return False
    
def obtener_lista_de_tipos(lista:list, clave:str)->set:
    '''Obtiene un set con las distintos tipos de la clave que se indique por párametro.'''
    tipos = []

    for heroe in lista:
        if clave in heroe:
            tipo = capitalizar_palabras(heroe[clave])
            if tipo:
                tipos.append(tipo)
            else:
                tipos.append("N/A")

    set_tipos = set(tipos)

    return set_tipos


def normalizar_dato_tp_5(dato:str, valor_x_defecto:str)->str:
    '''Normaliza el dato que se indique por párametro, si esta vacío retorna el valor por defecto y si no el dato.'''
    if not dato:
        return valor_x_defecto
    else:
        return dato
                         
def normalizar_heroe(heroe:dict, clave:str)->dict:
    '''Normaliza el dato de la clave del diccionario que se indican por párametro, si esta vacío coloca N/A retorna el diccionario con la modificacion'''
    valor_normalizar = heroe[clave]

    normalizacion = normalizar_dato_tp_5(valor_normalizar, "N/A")
    normalizacion = capitalizar_palabras(normalizacion)
    heroe["nombre"] = capitalizar_palabras(heroe["nombre"])
    heroe[clave]= normalizacion

    return heroe

def obtener_heroes_por_tipo(lista:list, set_tipos:set, clave:str)->dict:
    '''Obtiene un diccionario con los tipos y los nombres de los personajes que son de ese tipo'''
    dicc_pers_tipo = {}

    for tipo in set_tipos:
        dicc_pers_tipo[tipo] = []
    
    for heroe in lista:
        dato = heroe[clave]
        normalizado = normalizar_dato_tp_5(dato, "N/A")
        normalizado = capitalizar_palabras(normalizado)

        for tipo in set_tipos:

            if tipo == normalizado:
                dicc_pers_tipo[tipo].append(heroe["nombre"])

    return dicc_pers_tipo           

def guardar_heroe_por_tipo(dicc_tipos:dict, clave:str)->bool:
    '''Guarda en un archivo un string con los nombres de los personajes y el tipo al que corresponden. Si pudo guardar el archivo retorna true sino False'''
    mensaje = ""

    for tipo, heroes in dicc_tipos.items():

        if heroes:
            union_heroes = " | ".join(heroes)
            mensaje += f"{clave.capitalize()} {tipo}: {union_heroes}\n"
            
    print(mensaje)
    nombre_archivo = f"heroes_segun_{clave}.csv"
    guardar_ = guardar_archivo(nombre_archivo, mensaje)
    if guardar_archivo:
        return True
    else:
        return False

def stark_listar_heroes_por_dato(lista:list, clave:str)->bool:
    '''Lista personajes por tipo y guarda el archivo con los personajes. Si pudo guardarlo retorna True sino retorna False'''
    set_tipos = obtener_lista_de_tipos(lista, clave)
    dicc_tipos = obtener_heroes_por_tipo(lista, set_tipos, clave)
    guardar_heroes = guardar_heroe_por_tipo(dicc_tipos, clave)
 
    if guardar_heroes:
        return True
    else:
        return False

stark_marvel_app_5(lista_personajes)