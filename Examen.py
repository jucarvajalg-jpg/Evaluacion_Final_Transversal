# =====================================================================
# ASIGNATURA: Fundamentos de Programación (FPY1101)
# EVALUACIÓN: Evaluación Final Transversal (EFT) - PetMarket
# =====================================================================

#----------------------------------------------------------------------
# 1. Funcion de Validacion Independiente
#----------------------------------------------------------------------

def validar_codigo(codigo, productos):
    if not codigo or codigo.strip() == "":
        return False
    if codigo.strip().upper() in [k.upper() for k in productos.keys()]:
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

# ---------------------------------------------------------------------
# 3. PROGRAMA PRINCIPAL
# ---------------------------------------------------------------------

def main():
    productos = {
        'M001': ['Alimento Premium', 'comida', 'DogPlus', 10.0, True, False],
        'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 0.0, False, False],
        'M003': ['Snack Dental', 'snack', 'BiteJoy', 1.0, True, True],
        'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
        'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
        'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2.0, False, False]
    }

stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3]
}

while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Unidades por categoría")
        print("2. Búsqueda de productos por rango de precio")
        print("3. Actualizar precio de producto")
        print("4. Agregar producto")
        print("5. Eliminar producto")
        print("6. Salir")
        print("=====================================")

        opc = leer_opcion()

        if opc == -1:
            print("Opción no válida. Por favor, intente de nuevo.")
            continue
            
        if opc == 1:
            categoria = input("Ingrese la categoría a buscar: ")
            unidades_categorias(categoria, productos, stock)

        elif opc == 2:
            while True:
                try:
                    p_min = int(input("Ingrese el precio mínimo: "))
                    p_max = int(input("Ingrese el precio máximo: "))
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        break
                    else:
                        print("Debe ingresar valores validos (mínimo >= 0, máximo >= 0 y mínimo <= máximo). Intente de nuevo.")
                except ValueError:
                    print("Debe ingresar valores numéricos válidos. Intente de nuevo.")
            busqueda_precio(p_min, p_max, stock, productos)

        elif opc == 3:
            while True:
                cod = input("Ingrese el código del producto a actualizar: ")
                nuevo_p_str = input("Ingrese el nuevo precio: ")

                if validar_precio_val(nuevo_p_str):
                    nuevo_p = int(nuevo_p_str)
                    if actualizar_precio(cod, nuevo_p, stock, productos):
                        print(f"Precio del producto con código '{cod}' actualizado a {nuevo_p}.")
                    else:
                        print(f"No se encontró el producto con código '{cod}'.")
                else:
                    print("Precio inválido. Debe ser un número entero positivo.")
                
                resp = input("¿Desea actualizar otro producto? (s/n): ").strip().lower()
                if resp == 'n':
                    break

        elif opc == 4:
        
            cod = input("Ingrese código del producto: ")
            nom = input("Ingrese nombre: ")
            cat = input("Ingrese categoría: ")
            mar = input("Ingrese marca: ")
            pes = input("Ingrese peso (kg): ")
            imp = input("¿Es importado? (s/n): ")
            cac = input("¿Es para cachorro? (s/n): ")
            pre = input("Ingrese precio: ")
            uni = input("Ingrese unidades: ")

            if not validar_codigo(cod, productos):
                print("Código inválido o ya existe. Debe ser único y no vacío.")
            elif not validador_nombre(nom):
                print("Nombre inválido. No puede estar vacío.")
            elif not validar_categoria(cat):
                print("Categoría inválida. No puede estar vacía.")  
            elif not validar_marca(mar):
                print("Marca inválida. No puede estar vacía.")
            elif not validar_peso(pes):
                print("Peso inválido. Debe ser un número positivo.")
            elif not validar_es_importado(imp):
                print("Opción inválida para importado. Debe ser 's' o 'n'.")
            elif not validar_es_para_cachorros(cac):
                print("Opción inválida para cachorro. Debe ser 's' o 'n'.")
            elif not validar_precio_val(pre):
                print("Precio inválido. Debe ser un número entero positivo.")
            elif not validar_unidades_val(uni):
                print("Unidades inválidas. Debe ser un número entero positivo.")
            else:
                if agregar_productos(cod, nom, cat, mar, pes, imp, cac, pre, uni, productos, stock):
                    print(f"Producto '{nom}' agregado exitosamente.")
                else:
                    print("Error al agregar el producto. El código ya existe.")
        
        elif opc == 5:
            cod_eliminar = input("Ingrese el código del producto a eliminar: ")
            if eliminar_producto(cod_eliminar, productos, stock):
                print(f"Producto con código '{cod_eliminar}' eliminado exitosamente.")
            else:
                print(f"No se encontró el producto con código '{cod_eliminar}'.")

        elif opc == 6:
            print("Saliendo del programa. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()

    
