# =====================================================================
# ASIGNATURA: Fundamentos de Programación (FPY1101)
# EVALUACIÓN: Evaluación Final Transversal (EFT) - PetMarket
# =====================================================================

#----------------------------------------------------------------------
# 1. Funcion de Validacion Independiente
#----------------------------------------------------------------------

def validar_codigo(codigo, productos):
    if not codigo or codigo.scrip() == "":
        return False
    if codigo.strip().upper() in [k.upper( for k in productos.keys()]:
        return False
    return True

def validar_nombre(nombre):
    return bool(nombre and nombre.strip() != "")

def validar_categoria(categoria):
    return bool(categoria and categoria.strip() != "")

def validar_marca(marca):
    return bool(marca and marca.strip() != "")

def validar_peso(peso):
    try:
        val = float(peso)
        return val > 0
    except ValueError:
        return False

def validar_es_importado(opcion):
    return opcion.strip().lower() in ["s", "n"]

def validar_es_para_cachorros(opcion):
    return opcion.strip().lower() in ["s", "n"]

def validar_precio_val(precio):
    try:
        val = int(precio)
        return val > 0
    except ValueError:
        return False

def validar_unidades_val(unidades):
    try:
        val = int(unidades)
        return val > 0
    except ValueError:
        return False   

#----------------------------------------------------------------------
# 1. Funcion de Validacion Independiente
#----------------------------------------------------------------------

def leer_opcion():
    try:
        val = input("ingrese una opcion: ")
        opcion = int(val)
        if 1 <= opcion <= 6:
            return opcion
        else:
            return -1
    except ValueError:
        return -1

def buscar_codigo(codigo, productos):  
    return codigo.upper() in [k.upper() for k in productos.keys()]

def unidades_categorias(categorias, productos, stock):
    cat_buscar = categoria.strip().lower()
    total_unidades = 0

    for cod, info in productos.items():
        if info[1].lower() == cat_buscar:
            if cod in stock:
                total_unidades += stock[cod][1]

    print(f"El total de unidades disponibles para la categoría '{categoria}' es: {total_unidades}")


def busqueda_precio(p_min, p_max, stock, productos):
    resultados = []

    for cod, info_stock in stock.items():
        precio = info_stock[0]
        unidades = info_stock[1]

        if p_min <= precio <= p_max and unidades > 0:
            if cod in productos:
                nombre = productos[cod][0]
                resultados.append(f"{nombre} - Precio: {precio} - Unidades: {unidades}")

    if not resultados:
        print("No se encontraron productos en el rango de precio especificado.")

    else:
        resultados.sort()
        print("Los productos encontrados son: {resultados}")


def actualizar_precio(codigo, nuevo_precio, stock, productos):
    if buscar_codigo(codigo, productos):
        cod_upper = codigo.upper()

        key_exacta = next(k for k in stock.keys() if k.upper() == cod_upper)
        stock[key_exacta][0] = int(nuevo_precio)
        return True
    return False

def agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades, productos, stock):
    cod_upper = codigo.upper()
    if cod_upper in [k.upper() for k in productos.keys()]:
        return False
    
    imp_bool = True if es_importado.lower() == 's' else False
    cach_bool = True if es_para_cachorro.lower() == 's' else False
    
    productos[cod_upper] = [nombre, categoria, marca, float(peso_kg), imp_bool, cach_bool]
    stock[cod_upper] = [int(precio), int(unidades)]
    return True

def eliminar_producto(codigo, productos, stock):
    if buscar_codigo(codigo, productos):
        cod_upper = codigo.upper()
        key_p = next(k for k in productos.keys() if k.upper() == cod_upper)
        key_s = next(k for k in stock.keys() if k.upper() == cod_upper)
        del productos[key_p]
        del stock[key_s]
        return True
    return False
    